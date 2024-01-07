# from datetime import datetime
#
#
# class Human:
#     age: int
#
#     def __init__(self, age: int):
#         self.age = age
#
#     @classmethod
#     def from_birthday(cls, birthday_year: int):
#         this_year = datetime.now().year
#         return cls(this_year - birthday_year)
#
#
# person1 = Human(20)
# person2 = Human.from_birthday(2000)
# print(person2.age)



from datetime import datetime


class Human:
    age: int

    def __init__(self, age: int):
        self.age = age

    @classmethod
    def from_birthday(cls, birthday: str): #01.01.2000
        birthday=datetime.strptime(birthday, '%d.%m.%Y')
        this_year = datetime.now().year
        return cls(this_year - birthday.year)


person1 = Human(20)
person2 = Human.from_birthday('01.01.2000')
print(person2.age)
