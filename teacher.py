from person import Person


class Teacher(Person):
    """Teacher module with a few features"""

    def __init__(self, first_name, last_name, age, code, school_name='Undefined', star=0):
        """Initialize"""
        super().__init__(first_name, last_name, age, code)
        self.school_name = school_name
        self.star = star

    def return_features(self):
        """Returning features"""
        full_features = Person.return_features(self)
        adding_features = f' | School name : {self.school_name} | Star : {self.star}'
        full_features += adding_features
        return full_features
