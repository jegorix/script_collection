'''
Декоратор - это паттерн программирования, который позволяет добавлять
новый функционал к нашей функции, не видоизменяя саму функцию
'''

from typing import Callable
import time


def my_deco(func: Callable):
    def wrapper():
        start = time.time() 
        res = func()
        end = time.time()
        print(f"result = {end-start}")
        return res
    return wrapper


@my_deco
def my_func():
    time.sleep(1)
    return 124

my_func()