'''
Мне стало лень перегружать методы сравнения для каждого класса
и я решил сделать родительский класс в котором перегружу все необходимые методы
'''
class Man:

    def __lt__(self, other):
        if self._midl_grades() < other._midl_grades():
            return True
        else:
            return False

    def __gt__(self, other):
        if self._midl_grades() > other._midl_grades():
            return True
        else:
            return False

    def __le__(self, other):
        if self._midl_grades() <= other._midl_grades():
            return True
        else:
            return False

    def __ge__(self, other):
        if self._midl_grades() >= other._midl_grades():
            return True
        else:
            return False

    def __eq__(self, other):
        if self._midl_grades() == other._midl_grades():
            return True
        else:
            return False

    def __ne__(self, other):
        if self._midl_grades() != other._midl_grades():
            return True
        else:
            return False




class Student(Man):
    instances = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.instances.append(self)

    #Вспомогательный метод нахождения среднего значения оценки(используется в перегрузке метода __str__)

    def _midl_grades(self):
        all_grades = []
        courses = self.courses_in_progress + self.finished_courses
        for course in courses:
            if course in self.grades:
                all_grades += self.grades[course]
        midl_grade = sum(all_grades) / len(all_grades)
        return midl_grade

    def midl_grades_of_course(course):
        midl_grade_of_course = 0
        student_qnt = 0
        for student in Student.instances:
            if course in student.grades:
                midl_grade = sum(student.grades[course]) / len(student.grades[course])
                midl_grade_of_course += midl_grade
                student_qnt += 1
        if student_qnt != 0:
            return f'''Средняя оценка студентов по курсу {course} {midl_grade_of_course / student_qnt}'''
        else:
            return f'''По курсу {course} оценок нет'''

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        out = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашнее задание: {self._midl_grades()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}'''
        return out




class Mentor(Man):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor):
    instances = []
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
        self.instances.append(self)

    #Вспомогательный метод нахождения среднего значения оценки(используется в перегрузке метода __str__)

    def _midl_grades(self):
        all_grades = []
        #print(self.courses_attached)
        for course in self.courses_attached:
            if course in self.courses_attached:
                all_grades += self.grades[course]
        midl_grade = sum(all_grades) / len(all_grades)
        return midl_grade

    def __str__(self):
        out = f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self._midl_grades()}'''
        return out

    def midl_grades_of_course(course):
        midl_grade_of_course = 0
        lector_qnt = 0
        for student in Lecturer.instances:
            if course in student.grades:
                midl_grade = sum(student.grades[course]) / len(student.grades[course])
                midl_grade_of_course += midl_grade
                lector_qnt += 1
        if lector_qnt != 0:
            return f'''Средняя оценка лекторов по курсу {course} {midl_grade_of_course / lector_qnt}'''
        else:
            return f'''По курсу {course} оценок нет'''




class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    #Метод реализующий завершение курса обучения у студенета
    def end_course(self, student, course):
        if isinstance(student, Student) and course in student.courses_in_progress and course not in student.finished_courses:
            student.courses_in_progress.remove(course)
            student.finished_courses.append(course)

    def __str__(self):
        out = f'''Имя: {self.name}
Фамилия: {self.surname}'''
        return out






best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['PHP']
best_student.courses_in_progress += ['C++']

new_student = Student('Mark', 'West', 'man')
new_student.courses_in_progress += ['Python']
new_student.courses_in_progress += ['Java']

best_reviewer = Reviewer('Mike', 'Fitz')
best_reviewer.courses_attached += ['Python']
best_reviewer.courses_attached += ['Java']
best_reviewer.courses_attached += ['PHP']

best_lecture = Lecturer('Joe', 'Hasbrow')
best_lecture.courses_attached += ['Python']
best_lecture.courses_attached += ['Java']
best_lecture.courses_attached += ['C++']

new_lecture = Lecturer('Bob', 'Dillendzher')
new_lecture.courses_attached += ['Python']

#Выставление оценок студентам
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Java', 8)
best_reviewer.rate_hw(best_student, 'PHP', 7)
best_reviewer.rate_hw(best_student, 'PHP', 8)

best_reviewer.rate_hw(new_student, 'Python', 9)
best_reviewer.rate_hw(new_student, 'Python', 7)
best_reviewer.rate_hw(new_student, 'Python', 5)
best_reviewer.rate_hw(new_student, 'Python', 9)
best_reviewer.rate_hw(new_student, 'Java', 9)
best_reviewer.rate_hw(new_student, 'Java', 6)

#Выставление оценок лекторам
best_student.rate_lect(best_lecture, 'Python', 9)
best_student.rate_lect(best_lecture, 'Python', 8)
best_student.rate_lect(best_lecture, 'Python', 10)
best_student.rate_lect(best_lecture, 'Java', 9)
best_student.rate_lect(best_lecture, 'Java', 10)
best_student.rate_lect(best_lecture, 'Java', 10)
best_student.rate_lect(best_lecture, 'C++', 9)
best_student.rate_lect(new_lecture, 'Python', 8)

best_reviewer.end_course(best_student, 'Python')


print(best_student._midl_grades())
print(new_student._midl_grades())

print(best_student <= new_student)
print(best_student >= new_student)
print(best_student == new_student)
print(best_student != new_student)
print('*' * 20)

print(best_lecture._midl_grades())
print(new_lecture._midl_grades())

print(best_lecture > new_lecture)
print(best_lecture < new_lecture)
print(best_lecture == new_lecture)
print(best_lecture != new_lecture)

print('*' * 20)
print(best_student)
print('*' * 20)
print(best_reviewer)
print('*' * 20)
print(best_lecture)
print('*' * 20)
print(Student.midl_grades_of_course('Python'))
print(Lecturer.midl_grades_of_course('Python'))
