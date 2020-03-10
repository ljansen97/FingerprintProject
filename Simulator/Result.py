class Result:
    def __init__(self, filename, correct_image, accepted_by_algorithm, time):
        self.filename = filename
        self.accepted_by_algorithm = accepted_by_algorithm
        self.correct_image = correct_image
        self.time = time # in ms
        self.false_positive = accepted_by_algorithm and not correct_image