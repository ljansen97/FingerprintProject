import sys
from statistics import mean

import console_progressbar
import argparse
import os.path
import importlib.util
from Simulator import Simulator

DEFAULT_OPTIONS = {
    "algorithm_path": "./Algorithms/"
}

# Console parser
parser = argparse.ArgumentParser(description='Simulator to test the fingerprint recognition algorithm')
# Comparable argument
parser.add_argument('--comparable', dest='comparable', help='The file to be compared to the database', required=True)
# Database argument
parser.add_argument('--database', '-db', dest='database', help='Path to the database', required=True)
# Correct images argument
parser.add_argument('--correct', '-cf', action='append', dest='correct',
                    help='Filename of correct image in database folder', required=True)
# The algorithm path
parser.add_argument('--algorithm-path', dest='apath', help='The path in which the algorithm is located', required=False)
# The algorithm file
parser.add_argument('--algorithm', '-a', dest='algorithm',
                    help='Specify the algorithm to be used for this test (<AlgorithmName>.py must be available in Algorithm folder)',
                    required=True)
# Results in CSV
parser.add_argument('--csv', action='store_true', dest='csv', help='The CSV file all outputs are sent to',
                    required=False)
# Result image output folder
parser.add_argument('--output', '-o', dest='output',
                    help='If there is an output file, it will be written to this location')

parser.add_argument('--setting', '-s', dest='settings', action='append', help='Optional settings for the algorithm', required=False)

# Parse the arguments
args = parser.parse_args()

# Validate the arguments

#
# Validate comparable
#
if not os.path.exists(args.comparable):
    print("ERROR: Comparable file '" + args.comparable + "' does not exist exiting...")
    exit(-100)

#
# Validate database
#

# Check if database folder exists
if not os.path.exists(args.database):
    print("ERROR: Database folder '" + args.database + "' does not exist, exiting...")
    exit(-101)

# Check if database is empty
if len([name for name in os.listdir(args.database) if os.path.isfile(os.path.join(args.database, name))]) == 0:
    print("ERROR: Database folder is empty, exiting...")
    exit(-102)

#
# Correct images
#

# Check if image exists
for image in args.correct:
    filename = os.path.join(args.database, image)
    if not os.path.exists(filename):
        print("ERROR: Correct file '" + filename + "' doesn't exist, exiting...")
        exit(-103)

#
# Validate algorithm
#

# Default value of Algorithm path
if args.apath is None:
    args.apath = DEFAULT_OPTIONS["algorithm_path"]

if not os.path.exists(args.apath):
    print("ERROR: Algorithm folder '" + args.apath + "' folder does not exist, exiting...")
    exit(-104)

if not os.path.exists(os.path.join(args.apath, args.algorithm + ".py")):
    print("ERROR: " + args.apath + args.algorithm + ".py does not exist, exiting...")
    exit(-105)

#
# Output validation
#

# Check if folder exists
if args.output is not None:
    if not os.path.exists(args.output):
        print("ERROR: Output folder '" + args.output + "' does not exist, exiting...")
        exit(-106)

#
# ALL VALIDATIONS COMPLETED
#

# Import the algorithm
spec = importlib.util.spec_from_file_location(args.algorithm, os.path.join(args.apath, args.algorithm + ".py"))
algorithm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(algorithm)

exec("algorithm = algorithm." + args.algorithm + "()")

sim = Simulator(
    args.comparable,
    args.database,
    algorithm,
    args.correct,
    args.settings
)

sim.run()

# Calculate all results

amount_of_results = 0
amount_accepted_by_algorithm = 0
amount_correct = 0
amount_false_positives = 0
time_to_execute = []

for result in sim.results:
    time_to_execute.append(result.time)
    if result.accepted_by_algorithm:
        amount_accepted_by_algorithm += 1
        if result.correct_image:
            amount_correct += 1
    if result.false_positive:
        amount_false_positives += 1
    amount_of_results += 1

print("======================== TIMING STATS ========================")
print("Minimum time: %d ms" % (min(time_to_execute)))
print("Maximum time: %d ms" % (max(time_to_execute)))
print("Average time: %d ms" % (int(mean(time_to_execute))))
print("======================== RESULT STATS ========================")
print("Amount tested: %d" % amount_of_results)
print("Amount accepted by algorithm: %s (%.2f%% of all images)" % (
    amount_accepted_by_algorithm, (amount_accepted_by_algorithm / amount_of_results) * 100))
percentage_correct = (amount_correct / len(args.correct)) * 100
print("Amount correct: %d (%.2f%% of all images)" % (amount_correct, percentage_correct))
if amount_accepted_by_algorithm == 0:
    percentage_false_positive = 0
else:
    percentage_false_positive = (amount_false_positives / amount_accepted_by_algorithm) * 100
print("Amount of false positives: %d (%.2f%% of accepted)" % (amount_false_positives, percentage_false_positive))
print("====================== ACCEPTED FILES =======================")
for r in sim.results:
    if r.accepted_by_algorithm:
        print("- " + r.filename)
print("=============================================================")
