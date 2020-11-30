class Person:
    """Person and features"""

    def __init__(self, first_name='Undefined', last_name='Undefined', age=0, code='Undefined'):
        """Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.code = code

    def return_features(self):
        """Returning features"""
        full_features = f'Name is : {self.first_name} {self.last_name} | Age : {self.age} | Code : {self.code}'
        return full_features
