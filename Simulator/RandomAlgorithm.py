from Algorithm import Algorithm
from random import random
import time

class RandomAlgorithm(Algorithm):
    def test(self, path_to_comparable, path_to_compared):
        random_time = random()
        if(random_time > 0.6):
            random_time = 1 - random_time
        time.sleep(random_time)
        if path_to_compared == "00001013_plain_500_11_cropped11.bmp" or path_to_compared == "00001013_plain_500_03_cropped2.bmp":
            return True
        return (random() > 0.5) if True else False