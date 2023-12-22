class Student:
    name: str
    marks: list[int]
    _numb=2

    def addmark(self, mark):
        self.marks.append(mark)

    def __average(self):
        return sum(self.marks) / len(self.marks)

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __repr__(self):
        return self.name

    def __gt__(self, other):
        return self.__average() > other.__average()


class Group:
    name: str
    students: list[Student]

    def addstudent(self, student):
        self.students.append(student)

    def __average(self):
        marks = [mark for student in self.students for mark in student.marks]
        return sum(marks) / len(marks)

    def __repr__(self):
        return self.name

    def __init__(self, name, students):
        self.name = name
        self.students = students

    def __gt__(self, other):
        return self.__average() > other.__average()


st1 = Student('Mike', [3, 3, 3])
st2 = Student('Olga', [4, 4, 4])
st3 = Student('Nick', [5, 5, 5])

st4 = Student('Nina', [1, 2, 3])
st5 = Student('Bob', [5, 5, 5])
st6 = Student('Pet', [1, 1, 1])


def sort_students(*args):
    return sorted(args)


sl = sort_students(st1, st2)

# st1.addmark(6)

group1 = Group('Python-5', [st1, st2, st3])
group2 = Group('Python-4', [st4, st5, st6])

print(group1 > group2)

sorted_groups=sorted([group1, group2])
print(f'The best group is {sorted_groups[-1]}')

