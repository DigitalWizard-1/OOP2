from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ['Введение в программирование']
        self.courses_in_progress = ['Basic']
        self.grades = {}

    def rate_lec(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            print ('Ошибка')
            return

    def __str__(self):
        od = 0
        num = 0
        for id in self.grades:
            num += 1
            od += mean(self.grades[id])
        od = od / num

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {od}\n' \
              f'Курсы в процессе изучения: {str(self.courses_in_progress).strip("[]")}\n' \
              f'Завершенные курсы: {str(self.finished_courses).strip("[]")}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other,Student):
            print('ошибка сравнения')
            return
        else:
            comp_one = 0
            num=0
            for id in self.grades:
                num += 1
                comp_one += mean(self.grades[id])
            comp_one = comp_one / num
            comp_two = 0
            num = 0
            for id in other.grades:
                num += 1
                comp_two += mean(other.grades[id])
            comp_two = comp_two / num
            return comp_one<comp_two

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}



class Lecturer(Mentor):
    def __str__(self):
        od = 0
        num = 0
        for id in self.grades:
            num += 1
            od += mean(self.grades[id])
        od = od / num

        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {od}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other,Lecturer):
            print('ошибка сравнения')
            return
        else:
            comp_one = 0
            num=0
            for id in self.grades:
                num += 1
                comp_one += mean(self.grades[id])
            comp_one = comp_one / num
            comp_two = 0
            num = 0
            for id in other.grades:
                num += 1
                comp_two += mean(other.grades[id])
            comp_two = comp_two / num
            return comp_one<comp_two

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res=f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res

def StudentsAVG(stdlst,objectname):
    TempList=[]
    for id in stdlst:
        TempList += id.grades[objectname]
        TempListAVG = mean(TempList)
    return TempListAVG

def LectorsAVG(stdlst,objectname):
    TempList=[]
    for id in stdlst:
        TempList += id.grades[objectname]
        TempListAVG = mean(TempList)
    return TempListAVG


# заводим лучшего Студента
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
# заводим второго студента
student_two = Student('Vova', 'Oldboy', 'men')
student_two.courses_in_progress += ['Python']

# заводим проверяющего преподователя
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Basic']

# заводим лучшего лектора
cool_lector = Lecturer('Alex','Gendel')
cool_lector.courses_attached += ['Python']

# заводим второго лектора
lector_two = Lecturer('Second', 'Teacher')
lector_two.courses_attached += ['Python']

# ставим оценки студентам
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Basic', 7)
cool_reviewer.rate_hw(best_student, 'Basic', 9)

cool_reviewer.rate_hw(student_two, 'Python', 5)
cool_reviewer.rate_hw(student_two, 'Python', 6)
cool_reviewer.rate_hw(student_two, 'Python', 7)

# ставим оценки лекторам
best_student.rate_lec(cool_lector,'Python', 8)
best_student.rate_lec(cool_lector,'Python', 7)
best_student.rate_lec(cool_lector,'Python', 9)

best_student.rate_lec(lector_two,'Python', 8)
best_student.rate_lec(lector_two,'Python', 9)
best_student.rate_lec(lector_two,'Python', 10)

# задание 3.1 печать по формату
print(cool_reviewer)
print(cool_lector)
print(best_student)

# 3.2 сравниваем средние оценки студентов по дисциплинам
if student_two<best_student:
    print(f'Лучшие оценки у {best_student.name} {best_student.surname}')
else:
    print(f'лучшие оценки у {student_two.name} {student_two.surname}')

if lector_two<cool_lector:
    print(f'Лучшие оценки у {cool_lector.name} {cool_lector.surname}')
else:
    print(f'лучшие оценки у {lector_two.name} {lector_two.surname}')

#задание 4
StudentsList = [best_student,student_two]
LectorsList = [cool_lector,lector_two]
print("\nСредняя оценка студентов за курс Pyhon:",StudentsAVG(StudentsList,'Python'))
print("\nСредняя оценка лекторов за курс Pyhon:",LectorsAVG(LectorsList,'Python'))

