import sys
from console_progressbar import ProgressBar
from Simulator import Simulator
from Algorithm import Algorithm

# python Simulator.py teVergelijken.bmp D:/ProjectRedHat/vingerprints/ "correct_image1.bmp,correct_image2.bmp"
comparable = sys.argv[1]
fingerprints_dir = sys.argv[2]
correct_images = sys.argv[3].split(",")

print(correct_images)


algorithm = Algorithm()

sim = Simulator(comparable, fingerprints_dir, algorithm)

sim.run()