class Bottle:
    isopen = False  # open/closed
    amount = 100  # 0-100

    def open(self):
        self.isopen = True

    def close(self):
        self.isopen = False

    def check(self):
        if not self.isopen:
            print('Bottle is closed.')
            return False
        return True

    def drink(self, quantity):
        if self.check():
            if self.amount >= quantity:
                self.amount -= quantity
            else:
                print("Hey! We don't have that much.")

    def add(self, quantity):
        if self.check():
            if self.amount + quantity <= 100:
                self.amount += quantity
            else:
                print('Sorry, not enough space in the bottle.')


martini = Bottle()

print(martini.amount)
martini.open()
martini.drink(20)
print(martini.amount)
martini.drink(90)
print(martini.amount)
martini.add(40)
martini.add(10)
print(martini.amount)
martini.close()
martini.drink(20)
martini.add(20)

