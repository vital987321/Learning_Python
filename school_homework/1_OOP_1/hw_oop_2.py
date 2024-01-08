# task
# Создать классы Animal, Dog, Cat, DictMIxin
# Класс Animal, содержит информацию о том сколько у животного лап,
# какого оно цвета, как его зовут, и абстрактный метод speak.
# Для классов Dog и Cat, реализовать метод speak.
# В классе DictMixin реализовать метод который будет
# возвращать словарь с данными о конкретном животном.
# Примешать этот класс к собаке и коту

class Animal:
    name: str
    legs: int
    color: str

    def __init__(self, name, legs, color):
        self.name = name
        self.legs = legs
        self.color = color

    def speak(self):
        pass


class DictMixin():
    def info(self) -> dict:
        return {'name': self.name,
                'legs': self.legs,
                'color': self.color}


class Dog(Animal, DictMixin):
    def speak(self) -> None:
        print('waf!')


class Cat(Animal, DictMixin):
    def speak(self) -> None:
        print('Mau...')


puppy = Dog('Spark', 4, 'black')
kity = Cat('Mika', 4, 'white')

print(puppy.name)
print(puppy.info())
puppy.speak()
kity.speak()
