import sys
from console_progressbar import ProgressBar
from Simulator import Simulator
from RandomAlgorithm import RandomAlgorithm
from statistics import mean

# python main.py teVergelijken.bmp D:\ProjectRedHat\500\png\plain\converted "00001013_plain_500_03_cropped2.bmp,00001013_plain_500_11_cropped11.bmp"
comparable = sys.argv[1]
fingerprints_dir = sys.argv[2]
correct_images = sys.argv[3].split(",")

algorithm = RandomAlgorithm()

sim = Simulator(comparable, fingerprints_dir, algorithm, correct_images)

sim.run()

# Calculate all results

amount_of_results = 0
amount_accepted_by_algorithm = 0
amount_correct = 0
amount_false_positives = 0
time_to_execute = []

for result in sim.results:
    time_to_execute.append(result.time)
    if(result.accepted_by_algorithm):
        amount_accepted_by_algorithm += 1
        if(result.correct_image):
            amount_correct += 1
    if(result.false_positive):
        amount_false_positives += 1
    amount_of_results += 1
    
print("======================== TIMING STATS ========================")
print("Minimum time: %d ms" % (min(time_to_execute)))
print("Maximum time: %d ms" % (max(time_to_execute)))
print("Average time: %d ms" % (int(mean(time_to_execute))))
print("======================== RESULT STATS ========================")
print("Amount tested: %d" % amount_of_results)
print("Amount accepted by algorithm: %s (%.2f%% of all images)" % (amount_accepted_by_algorithm, (amount_accepted_by_algorithm / amount_of_results) * 100))
percentage_correct = (amount_correct / len(correct_images)) * 100
print("Amount correct: %d (%.2f%% of all images)" % (amount_correct, percentage_correct))
percentage_false_positive = (amount_false_positives / amount_accepted_by_algorithm) * 100
print("Amount of false positives: %d (%.2f%% of accepted)" % (amount_false_positives, percentage_false_positive))
print("==============================================================")