class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        # print("Создан Student: {0}".format(self.name, self.surname))

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    # способность студентов ставить оценки лекторам
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.grades += [grade]
        else:
            return "Ошбика"

    # высчитываем среднюю оценку студентов
    def get_avg_grade(self):
        sum_hw = 0
        count = 0
        for grades in self.grades.values():
            sum_hw += sum(grades)
            count += len(grades)
        return round(sum_hw / count, 2)

    # перезагружаем str
    def __str__(self):
        res = f"Студент: \n\
            Имя: {self.name} \n\
            Фамилия: {self.surname} \n\
            Средняя оценка за ДЗ: {self.get_avg_grade()} \n\
            Курсы в процессе изучения: {self.courses_in_progress} \n\
            Завершенные курсы: {self.finished_courses} \n"

        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print("Такого студента нет")
            return
        else:
            compare = self.get_avg_grade() < other_student.get_avg_grade()
            if compare:
                print(f'{self.name} {self.surname} учится хуже, чем {other_student.name} {other_student.surname}')
            else:
                print(f'{other_student.name} {other_student.surname} учится хуже, чем {self.name} {self.surname}')
        return compare

#Родительский класс Менторы
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        # print("Создан Mentor: {0}".format(self.name))

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

#дочерний класс - проверяющие
class Reviewer(Mentor):

    # Менторы оценивают студентво
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

        res = f"Имя: {self.name}\n\
          Фамилия: {self.surname}\n"

    def __str__(self):
        return res


#дочерний класс - Лекторы
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        # print("Создан Лектор: {0}".format(self.name))

    def __str__(self):
        res = f"Лектор: \n\
                Имя: {self.name} \n\
                Фамилия: {self.surname} \n\
                Средняя оценка от студентов: {sum(self.grades) / len(self.grades) :.2f} \n"
        return res

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print("Такого лектора нет")
            return
        else:
            compare = sum(self.grades) / len(self.grades) < sum(other_lecturer.grades) / len(other_lecturer.grades)
            if compare:
                print(
                    f'{self.name} {self.surname}  не такой хороший лектор, как {other_lecturer.name} {other_lecturer.surname}')
            else:
                print(
                    f'{self.name} {self.surname}  как лектор лучше, чем {other_lecturer.name} {other_lecturer.surname}')
            return compare

#функция для подсчета средней оценки по всем студентам
def get_avg_hw_grade(student_list, course):
    total_sum = 0

    for student in student_list:
        for kurs, grades in student.grades.items():
            if kurs == course:
                total_sum += sum(grades) / len(grades)
        return round(total_sum / len(student_list), 2)


#функция для подсчета средней оценки по всем лекторам
def get_avg_lect_grade(lect_list):
    total_sum = 0

    for lecturer in lect_list:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)

    return round(total_sum / len(lect_list), 2)






best_student = Student('Roy', 'Beng', 'man')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ["Git"]

next_student = Student("Peter", "Shulte", "man")
next_student.courses_in_progress += ['Python']
next_student.courses_in_progress += ['Git']


cool_reviewer = Reviewer("Frank", "Wain")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 6)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 8)

cool_reviewer.rate_hw(next_student, 'Python', 9)
cool_reviewer.rate_hw(next_student, 'Python', 9)
cool_reviewer.rate_hw(next_student, 'Python', 10)

cool_reviewer.rate_hw(best_student, 'Git', 9)
cool_reviewer.rate_hw(best_student, 'Git', 9)

cool_lecturer = Lecturer("Lector", "Trektor")
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']

next_lecturer = Lecturer("Nextor", "Vektor")
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']

best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student.rate_lecturer(cool_lecturer, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Git', 6)
best_student.rate_lecturer(next_lecturer, 'Python', 5)
best_student.rate_lecturer(next_lecturer, 'Python', 8)
best_student.rate_lecturer(next_lecturer, 'Python', 6)
best_student.rate_lecturer(next_lecturer, 'git', 9)
print(next_lecturer.grades)
print(cool_lecturer.grades)

# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# cool_mentor.courses_attached += ['Pythonka']

# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Pythonka', 100)

# print(best_student.grades)

print(cool_lecturer)
print(next_lecturer)

print(best_student)
print(next_student)

print(best_student.grades)
print(next_student.grades)

print(best_student > next_student)

print(cool_lecturer.grades)
print(next_lecturer.grades)


print(cool_lecturer > next_lecturer)

#вызов функции подсчета средней оценки по всем студентам по курсу
print(get_avg_hw_grade([best_student, next_student], "Python"))

#вызов функции подсчета средней оценки по всем лекторам по курсу
print(get_avg_lect_grade([cool_lecturer, next_lecturer]))