class Student:
    instances = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.instances.append(self.name + ' ' + self.surname)

    #Вспомогательный метод нахождения среднего значения оценки(используется в перегрузке метода __str__)
    def _midl_grades(self):
        all_grades = []
        courses = self.courses_in_progress + self.finished_courses
        for course in courses:
            all_grades += self.grades[course]
        midl_grade = sum(all_grades) / len(all_grades)
        return midl_grade

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {self._midl_grades()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)} '''

    def __lt__(self, other):
        if self._midl_grades() < other._midl_grades():
            return True
        else:
            return False


class Mentor:
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
        self.instances.append(self.name)

    #Вспомогательный метод нахождения среднего значения оценки(используется в перегрузке метода __str__)
    def _midl_grades(self):
        all_grades = []
        #print(self.courses_attached)
        for course in self.courses_attached:
            #print(course)
            all_grades += self.grades[course]
        midl_grade = sum(all_grades) / len(all_grades)
        return midl_grade

    def __str__(self):
        return f'''Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._midl_grades()}'''


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
        return f'''Имя: {self.name}\nФамилия: {self.surname}'''



best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['PHP']

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
#best_lecture.courses_attached += ['PHP']


#Выставление оценок студентам
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Java', 8)
best_reviewer.rate_hw(best_student, 'PHP', 7)

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
best_student.rate_lect(best_lecture, 'C++', 9)

best_reviewer.end_course(best_student, 'Python')

#print(best_student.grades)
#print(best_lecture.grades)
#best_student._midl_grades()

print(best_student < new_student)
print(Student.instances)

'''
print(best_reviewer)
print('*' * 20)
print(best_lecture)
print('*' * 20)
print(best_student)
'''
'''
print(best_student.grades)
print(best_lecture.courses_attached)
print(best_lecture.grades)
'''