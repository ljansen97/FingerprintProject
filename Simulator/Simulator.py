from Algorithm import Algorithm
from Result import Result
import os
import time
from console_progressbar import ProgressBar


class Simulator:
    def __init__(self, comparable, fingerprints_dir, algorithm, correct_images, settings):
        self.comparable = comparable
        self.fingerprints_dir = fingerprints_dir
        self.algorithm = algorithm
        self.correct_images = correct_images
        self.settings = settings
        # List with times per try
        self.times = []
        # List with results
        self.results = []
        # Get the files
        self.files = [item for item in os.listdir(self.fingerprints_dir) if
                      os.path.isfile(os.path.join(self.fingerprints_dir, item))]
        # Progress bar
        self.progress = ProgressBar(total=len(self.files), prefix='Checking', suffix='', decimals=2, length=50,
                                    fill='#', zfill='.')

    def run(self):
        print("===================== RUNNING (%s files) ======================" % (len(self.files)))

        count = 0

        if not isinstance(self.algorithm, Algorithm):
            raise Exception("Wrong datatype for algorithm")

        for file in self.files:
            starttime = int(round(time.time() * 1000))
            accepted = self.algorithm.test(self.comparable, os.path.join(self.fingerprints_dir, file), self.settings)
            endtime = int(round(time.time() * 1000))
            time_to_execute = endtime - starttime

            count += 1

            self.progress.print_progress_bar(count)

            self.results.append(Result(file, file in self.correct_images, accepted, time_to_execute))