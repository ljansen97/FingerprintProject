import sys
from console_progressbar import ProgressBar
from Simulator import Simulator
from Algorithm import Algorithm

# python Simulator.py teVergelijken.bmp D:/ProjectRedHat/vingerprints/
comparable = sys.argv[1]
fingerprints_dir = sys.argv[2]

algorithm = Algorithm()



sim = Simulator(comparable, fingerprints_dir, algorithm)

sim.run()