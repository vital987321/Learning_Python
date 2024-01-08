# task
#
# Создаем структуру для группы студентов
# 1.1) Класс студент, содержит поля name и marks, для хранения имени и оценок
# 1.2) Метод для подсчета среднего балла студента
# 1.3) Метод для добавления оценки студенту
# 1.4) Magic метод(ы) для сравнения двух студентов по среднему баллу
# 1.5) Класс группы, который содержит поля name и students, для хранения названия группы и студентов группы
# 1.6) Метод для подсчета среднего балла группы который является средним баллом из всех средних баллов студентов учащихся в этой группе
# 1.7) Метод для добавления студента в группу
# 1.8) Magic метод(ы) для сравнения двух групп
# 1.9) Написать функцию которая принимает список групп, а возвращает самую успешную и самую не успешную группу


class Student:
    name: str
    marks: list[int]

    def __init__(self, name: str, marks: iter) -> None:
        self.name = name
        self.marks = list(marks)

    def __str__(self):
        return self.name

    def __average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def addmakr(self, mark: int) -> None:
        self.marks.append(mark)

    def __gt__(self, other) -> bool:
        return self.__average() > other.__average()


class Group:
    name: str
    students: list[Student]

    def __init__(self, name, students: iter):
        self.name = name
        self.students = list(students)

    def __str__(self):
        return self.name

    def __average(self) -> float:
        marks = [mark for student in self.students for mark in student.marks]
        return sum(marks) / len(marks)

    def addstudent(self, student: Student) -> None:
        self.students.append(student)

    def __gt__(self, other) -> bool:
        return self.__average() > other.__average()


def bestworstgroup(groups: iter) -> tuple[Group, Group]:
    # Влад, вопрос по анотированю для этой функции. Если указать тип (groups: list[Group]),
    # то сразу понятно какие елементи списка будут использоваться (Group).
    # Но я хочу не list, а любой итерируэмый обьект. iter[Group] - не работает.
    # Как правильно написать? Есть вообще такой тип данных, как любой итерируэмый обьект?
    groups = sorted(list(groups))
    return groups[0], groups[-1]


student1 = Student('Mike', (2, 2, 2, 2, 2, 2))
student2 = Student('Nick', [2, 3, 2, 3, 2, 3, 2])
student3 = Student('Lisa', (4, 5, 4, 5, 4, 5, 4))
student4 = Student('Olga', [5, 5, 5, 5, 5])
gr1 = Group('gA', (student1, student2))
gr2 = Group('gB', (student3,))
gr2.addstudent(student4)

worst, best = bestworstgroup((gr1, gr2))
print(f'The best group is {best}, the worst is {worst}.')
