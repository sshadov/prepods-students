# def average_grade(_dict): #считает среднюю оценку преподавателя/студента
#     summ_grade = 0
#     counter_grade = 0
#     for grade in _dict:
#         summ_grade += grade
#         counter_grade += 1
#         average = summ_grade / counter_grade
#     return average

# def average_grade_stud(students_list, course): #считает среднюю оценку за курс у студентов
#     summ_grades = 0
#     counter_grades = 0
#     for student in students_list:
#         summ_grades += student.grades[course]
#         counter_grades += 1
#         _average_grade = summ_grades / counter_grades
#     return _average_grade
#
# def average_grade_lect(lectors_list, course): #считает среднюю оценку за курс у преподавателей
#     summ_grades = 0
#     counter_grades = 0
#     for lector in lectors_list:
#         summ_grades += lector.grades[course]
#         counter_grades += 1
#         _average_grade = summ_grades / counter_grades
#     return _average_grade

def average_grade_human(humans_list, course): #считает среднюю оценку за курс у списка преподавателей или студентов
    summ_grades = 0
    counter_grades = 0
    for human in humans_list:
        summ_grades += human.grades[course]
        counter_grades += 1
        _average_grade = summ_grades / counter_grades
    return _average_grade


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):  # считает среднюю оценку студента
        values = self.grades.values()
        summ_grade = 0
        counter_grade = 0
        for grade in values:
            summ_grade += grade
            counter_grade += 1
            average = summ_grade / counter_grade
        return average

    def __str__(self): #Делаем вывод всех данных о студенте через print() {average_grade(self.grades.values())}
        # res = print(*self.finished_courses, sep=',')
        res = f'Имя: {self.name} \n ' \
              f'Фамилия: {self.surname}\n ' \
              f'Средняя оценка за домашнии задания: {self.average_grade()}\n ' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n ' \
              f'Пройденныея курсы: {", ".join(self.finished_courses)}'
        return res

    def rate_lecturer(self, lecturer, course, grade): #оцениваем лекторов
        if isinstance(lecturer, Lecturer) and (course in self.finished_courses or course in self.courses_in_progress) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            print('Ошибка')

    def __lt__(self, other): #сравниваем студентов по средней оценке
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):  # считает среднюю оценку преподаватедя
        values = self.grades.values()
        summ_grade = 0
        counter_grade = 0
        for grade in values:
            summ_grade += grade
            counter_grade += 1
            average = summ_grade / counter_grade
        return average

    def __str__(self): #Вывод всех данных о преподавателе через print()
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n Средняя оценка {self.average_grade()}'
        return  res

    def __lt__(self, other): #сравниваем лекторов по средней оценке
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self.average_grade() < self.average_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.courses_attached = []



    def rate_hw(self, student, course, grade): #выставляем студентам оценки за курс
        if isinstance(student, Student) and (course in self.courses_attached) and (course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self): #вывод данных о ревьювере через print()
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return  res


stepanrazin = Student('Stepan', 'Razin', 'male')
stepanrazin.finished_courses = ['Git']
stepanrazin.courses_in_progress = ['python']
stepanrazin.grades = {'Git': 10, 'rzhd': 6}

annakarenina = Student('Anna', 'Karenina', 'female')
annakarenina.finished_courses = ['rzhd', 'anatomy']
annakarenina.courses_in_progress = ['python']
annakarenina.grades = {'rzhd': 4, 'anatomy': 8}

ivanpetrov = Mentor('ivan', 'petrov')
peterivanov = Mentor('peter', 'ivanov')

drDulittle = Lecturer('dr', 'dulittle')
drDulittle.courses_attached = ['rzhd', 'python']
drDulittle.grades = {'rzhd': 8, 'python': 9, 'Git': 7}

kosanostra = Lecturer('Kosa', 'nostra')
kosanostra.courses_attached = ['Git', 'anatomy']
kosanostra.grades = {'Git': 10, 'anatomy': 7}

kavabanga = Reviewer('Kava', 'Banga')
kavabanga.courses_attached = ['python', 'Git']

balabol = Reviewer('Bala', 'Bol')
balabol.courses_attached = ['rzhd', 'anatomy']

annakarenina.rate_lecturer(drDulittle, 'rzhd', 10) #студент оценивает преподавателя

kavabanga.rate_hw(stepanrazin, 'Git', 7) #преподаватель оценивает студента

print(annakarenina) #вывод студента

students_list = [annakarenina, stepanrazin]
lectors_list = [drDulittle, kosanostra]

print('__________________')
print('Сравнение студентов:', annakarenina > stepanrazin) #сравнение средних оценок студентов
print('__________________')
print('Сравнение лекторов:', kosanostra > drDulittle) #сравнение средних оценок лекторов
print('__________________')
print(average_grade_human(students_list, 'rzhd')) #средние оценки за курс
print(average_grade_human(lectors_list, 'Git'))