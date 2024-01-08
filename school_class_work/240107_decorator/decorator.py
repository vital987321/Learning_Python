from time import sleep
from datetime import datetime


def decorator(func):
    def wrap():
        print('Decorator start')
        start = datetime.now()
        func()
        print('Decorator finish')
        print('Executed time:',datetime.now() - start)

    return wrap


@decorator
def myfunc():
    print('Function start')
    sleep(3)
    print('Function finish')

a=1
# myfunc()

