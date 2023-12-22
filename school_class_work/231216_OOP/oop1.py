class Phone:
    number = '000000'
    __calls_counter = 0

    def set_number(self, num):
        self.number = num

    def accept_call(self):
        self.__calls_counter += 1

    def calls_amount(self):
        return self.__calls_counter


nokia = Phone()
samsung = Phone()
lg = Phone()

nokia.set_number('777-777-777')
samsung.set_number('888-888-888')
lg.set_number('999-999-999')

nokia.accept_call()
nokia.accept_call()
samsung.accept_call()


def total_calls(phones: list[Phone]) -> int:
    return sum([ph.calls_amount() for ph in phones])


phones = [nokia, samsung, lg]

print(total_calls(phones))

