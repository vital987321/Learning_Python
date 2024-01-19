class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

@property
def full_name(self):
    return f"{self.first_name} {self.last_name}"

person = Person("Mike", "Driscoll")

print(person.first_name)        # Mike
print(person.full_name)         # Mike Driscoll

person.full_name = "Jackalope"  # AttributeError