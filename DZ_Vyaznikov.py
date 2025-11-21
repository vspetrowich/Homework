class Student:
    def __init__(self, name, family, gender):
        self.name = name
        self.family = family
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.spisok = []


    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, student, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)  and  course in lecturer.courses_attached and
                course in student.courses_in_progress):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'



    def homework(self):
        count = 0
        sum = 0
        sred = float()
        sred = 0.0
        for key, val in self.grades.items():
            for znach in val:
                count += 1
                sum += znach
        if count != 0:
            sred = sum / count
        return round(sred,1)


    def __str__(self):
        count = 0
        sum = 0
        sred = float()
        sred = 0.0
        for key,val in self.grades.items():
            for znach in val:
                count +=1
                sum += znach
        if count != 0 :
            sred = sum/count
        return (f"Имя:{self.name}\nФамилия: {self.family}\n"
                f"Средняя оценка за домашние задания: {round(sred,1)}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def ocenki_po_course(stud1, course):
        stud = stud1
        list1 = []
        list1 = stud.grades.get(course)
        return list1


    # def sred_ocenka(self, spisok):
    #     print(spisok)
    #     #print(course)
    #     return


class Mentor:
    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.courses_attached = []



class Lecturer (Mentor):
    def __init__(self, name, family):
        super().__init__(name, family)
        self.grades = {}
        #self.courses_attached = []

    def __str__(self):
        count = 0
        sum = 0
        sred = 0.0
        for key,val in self.grades.items():
            for znach in val:
                count +=1
                sum += znach
        if count != 0 :
            sred = sum/count
        return (f"Имя:{self.name}\nФамилия: {self.family}"
                f"\nСредняя оценка за лекции: {round(sred,1)}")

    def lecture(self):
        count = 0
        sum = 0
        sred = 0.0
        for key, val in self.grades.items():
            for znach in val:
                count += 1
                sum += znach
        if count != 0:
            sred = sum / count
        return round(sred,1)

class Reviewer(Mentor):
    def __init__(self, name, family):
        super().__init__(name, family)
        #self.courses_attached = []

    def grades_add(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and
                course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя:{self.name}\nФамилия: {self.family}")


class Sravni_st:
    def  __init__(self, persona1, persona2):
        self.persona1 = persona1
        self.persona2 = persona2
        itog = ''
        #print(Student.homework(self.persona1))
        #print(Student.homework(self.persona2))
        if Student.homework(self.persona1) > Student.homework(self.persona2):
            itog = (f"Средний бал выше у студента: Имя:{self.persona2.name}"
                    f" Фамилия: {self.persona1.family}"
                    f"{Student.homework(self.persona1)} ")
        elif Student.homework(self.persona1) < Student.homework(self.persona2):
            itog = (f"Средний бал выше у студента: {self.persona2.name}"
                    f" {self.persona2.family} "
                    f"{Student.homework(self.persona2)} ")
        else:
            itog = (f"Оценки у студентов равны: {Student.homework(self.persona1)}")
        print(itog)
        return

class Sravni_lec:
    def  __init__(self, persona1, persona2):
        self.persona1 = persona1
        self.persona2 = persona2
        itog = ''
        if Lecturer.lecture(self.persona1) > Lecturer.lecture(self.persona2):
            itog = (f"Средний бал выше у лектора: {self.persona1.name}"
                    f" {self.persona1.family}"
                    f" {Lecturer.lecture(self.persona1)} ")
        elif Lecturer.lecture(self.persona1) < Lecturer.lecture(self.persona2):
            itog = (f"Средний бал выше у лектора: {self.persona2.name}"
                    f" {self.persona2.family} "
                    f"{Lecturer.lecture(self.persona2)} ")
        else:
            itog = (f"Оценки у лекторов равны: {Lecturer.lecture(self.persona1)}")
        print(itog)
        return

class Sred_ocenka:
    def __init__(self, spisok, course):
        self.course = course
        count = 0
        sred = 0.0
        if isinstance(spisok[0], Student):
            for znach in spisok:
                list1 = Student.ocenki_po_course(znach, course)
                if list1 is not None:
                    sred += sum(list1)/len(list1)
                    count += 1
            if count != 0:
                sred = sred / count
            print(f"Средняя оценка студентов по курсу: {course} = {round(sred,1)}")
        elif isinstance(spisok[0], Lecturer):
            for znach in spisok:
                list1 = Student.ocenki_po_course(znach, course)
                if list1 is not None:
                    sred += sum(list1)/len(list1)
                    count += 1
            if count != 0:
                sred = sred / count
            print(f"Средняя оценка лекторов по курсу: {course} = {round(sred,1)}")
        else :
            print(f"Оценок по курсу : {course} нет")
        return





# задание 1
lecturer2 = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer2, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer2.courses_attached)    # []
print(reviewer.courses_attached)    # []

# задание 2
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
student.finished_courses += ['Git']
student.grades['Java'] = [10, 9, 5, 8]
student.grades['Python'] = [7, 8, 8]

lecturer2.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(student, lecturer2, 'Python', 7))  # None
print(student.rate_lecture(student, lecturer2, 'Java', 8))  # Ошибка
print(student.rate_lecture(student, lecturer2, 'C++', 9))  # Ошибка
print(student.rate_lecture(student, reviewer, 'Python', 6))  # Ошибка
print(lecturer2.grades)  # {'Python': [7]}

# задание 3
print(reviewer)
print(lecturer2)
print(student)

# добавляем второго студента
student1 = Student('Иван', 'Воронков', 'М')

student1.finished_courses += ['Git']
student1.courses_in_progress += ['Python', 'C++']
student1.grades['Python'] = [8, 9, 8]
student1.grades['C++'] = [9, 9, 10]
print('Выводим информацию про второго студента для статистики :')
print(student1)
# задание 3 часть 2 сравниваем студентов
# print(student1.homework())
# print(student.homework())
Sravni_st(student, student1)

# добавляем 2-го лектора и 2-го эксперта
lecturer1 = Lecturer('Антон', 'Павлов')
reviewer1 = Reviewer('Денис', 'Смирнов')
# добавляем курсы преподавателей
lecturer1.courses_attached += ['Python', 'Java']
reviewer1.courses_attached += ['Python', 'Git']
# выставляем оценки за лекции
print('выставляем оценки за лекции для статистики :')
print(student.rate_lecture(student, lecturer1, 'Java', 9)) # None
print(student.rate_lecture(student, lecturer1, 'Python', 8)) # None
print(student1.rate_lecture(student1, lecturer2, 'Python', 8)) # None
print(student1.rate_lecture(student1, lecturer2, 'C++', 9)) # None

#задание 3 часть 2 сравниваем лекторов
Sravni_lec(lecturer2, lecturer1)

#задание 4 средняя оценка за ДЗ по конкретному курсу
Sred_ocenka([student, student1], 'Python')
#задание 4 средняя оценка за лекции по конкретному курсу
Sred_ocenka([lecturer1, lecturer2], 'Python')

