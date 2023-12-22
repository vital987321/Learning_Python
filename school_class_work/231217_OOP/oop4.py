
import random


class Person:
    def __init__(self, firstName, lastName, age):
        # public properties
        self.firstName = firstName
        self.lastName = lastName
        # protecte properties
        self._age = age
        # private properties
        self.__personID = random.randint(1, 100)
        # private methods

    def __showID(self):
        print(self.__personID)

    # public methods
    def getInfo(self):
        self.__showID()
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

    def sayHi(self, msgText):
        print(self.getInfo())
        return f"{msgText}! I am {self.firstName}."

    # static methods
    @staticmethod
    def sayGreetings():
        print("Nice to meet you!")


person1 = Person("Joe", "Black", 30)
person1.sayGreetings()