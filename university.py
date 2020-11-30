from student import Student
from teacher import Teacher


class University:
    """University management of student and teacher"""

    def __init__(self, name_tc):
        """Initialize"""
        self.name_tc = name_tc
        self.students = []
        self.teachers = []

    def add_student(self, Student):
        """Adding student"""
        self.students.append(Student)

    def add_teacher(self, Teacher):
        """Adding teacher"""
        self.teachers.append(Teacher)

    def remove_student(self, name_student='NULL'):
        """Remove student"""
        counter = 0
        for student in self.students:
            if student.first_name == name_student:
                del self.students[counter]
                break
            counter += 1

    def remove_teacher(self, name_teacher='NULL'):
        """Remove teacher"""
        counter = 0
        for teacher in self.teachers:
            if teacher.first_name == name_teacher:
                del self.teachers[counter]
                break
            counter += 1

    def student_features(self):
        """Returning features of students"""
        full_students_features = f'Name Of University: {self.name_tc}\n\r'
        for student in self.students:
            full_students_features += student.return_features()
            full_students_features += '\n\r'
        return full_students_features

    def teacher_features(self):
        """Returning features of teachers"""
        full_teachers_features = f'Name Of University: {self.name_tc}\n\r'
        for teacher in self.teachers:
            full_teachers_features += teacher.return_features()
            full_teachers_features += '\n\r'
        return full_teachers_features

    def rank_students(self):
        """Rank Students of scores and calculation average"""
        rank = 0
        count_of_scores = 0
        for student in self.students:
            for score in student.scores:
                rank += score
                count_of_scores += 1
        calc = rank / count_of_scores
        return calc

    def stars_teachers(self):
        """Stars of teachers"""
        star = 0
        for teacher in self.teachers:
            star += teacher.star
        calc = star / len(self.teachers)
        return calc


university = University('Mohajer tc')

university.add_student(Student('Ali', 'Hajihashemi', 14,
                               '113123456', [20, 15, 19, 14, 17, 20, 20, 20]))
university.add_student(Student('Amir', 'Hosseini', 12,
                               '114021250', [20, 19, 19, 18, 19, 20, 20, 20]))
university.add_student(Student('Satar', 'Salehi', 19,
                               '115123111', [18, 20, 19, 14, 17, 20, 20, 15]))

university.add_teacher(Teacher('Ali', 'Hajihashemi', 22,
                               '113123456', 'Mohajer tc', 5))
university.add_teacher(Teacher('Amir', 'Hosseini', 25,
                               '114021250', 'Mohajer tc', 5))
university.add_teacher(Teacher('Satar', 'Salehi', 26,
                               '115123111', 'Mohajer tc', 5))

# university.remove_teacher('Satar')
# university.remove_student('Ali')

s = university.student_features()
t = university.teacher_features()
r = university.rank_students()
r = round(r, 2)
ss = university.stars_teachers()

print(s)

print('----------------------------------')

print(t)

print('----------------------------------')

print(r)

print('----------------------------------')

print(ss)
