from person import Person


class Student(Person):
    """Student module with features"""

    def __init__(self, first_name, last_name, age, code, scores):
        """Initialize"""
        # Adding parent init
        super().__init__(first_name, last_name, age, code)
        self.scores = scores

    def average(self):
        """Average of scores"""
        sum_of_numbers = 0
        for score in self.scores:
            sum_of_numbers += score
        avg = sum_of_numbers / len(self.scores)
        avg = round(avg, 2)
        return avg

    def return_features(self):
        """Returning features"""
        full_features = Person.return_features(self)
        adding_features = f' | Average : {self.average()}'
        full_features += adding_features

        return full_features
