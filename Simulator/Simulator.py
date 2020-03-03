from Algorithm import Algorithm
import os

class Simulator:
	def __init__(self, comparable, fingerprints_dir, algorithm):
		self.comparable = comparable
		self.fingerprints_dir = fingerprints_dir
		self.algorithm = algorithm
		# List with times per try
		self.times = []
		# List with results
		self.results = []
		# Get the files
		self.files = [item for item in os.listdir(self.fingerprints_dir) if os.path.isfile(os.path.join(self.fingerprints_dir, item))]
		self.number_of_files = len(self.files)
		
	def getNumberOfItems(self):
		return self.number_of_items
		
	def getFingerprintsDir(self):
		return self.fingerprints_dir
		
	def getComparable(self):
		return comparable
		
	def getTimes(self):
		return self.times
		
	def getResults(self):
		return self.results
		
	def run(self):
		print("Running simulator")
	
		if not isinstance(self.algorithm, Algorithm):
			raise Exception("Wrong datatype for algorithm")
		
		
		for file in self.files:
			self.algorithm.test(self.comparable, file)