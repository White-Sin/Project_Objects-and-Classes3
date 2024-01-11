class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}




    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"


    def average_grade(self):
        total_grades = 0
        num_grades = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            num_grades += len(grades_list)
        if num_grades > 0:
            return round(total_grades / num_grades, 1)
        else:
            return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"


    def average_grade(self):
        total_grades = 0
        num_grades = 0
        for grades_list in self.grades.values():
            total_grades += sum(grades_list)
            num_grades += len(grades_list)
        if num_grades > 0:
            return round(total_grades / num_grades, 1)
        else:
            return 0



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'




some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses = ['Введение в програмирование']

some_reviewer.rate_hw(some_student, 'Python',  9.8)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_lecturer.rate_hw(some_student, 'Python', 10)
some_lecturer.rate_hw(some_student, 'Python', 9.8)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
