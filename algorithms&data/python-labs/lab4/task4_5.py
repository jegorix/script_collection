# 4.	Пусть задан класс Point, описывающий точку х;у на координатной плоскости. 
# Используя механизм наследования, расширьте возможности класса Point путем добавления 
# нового атрибута цвета, реализовав при этом подкласс PointColor. В классе Point реализуйте следующие атрибуты:
# •	координаты точки;
# •	метод инициализации, который получает два параметра – координаты точки х;у;
# •	метод вычисления расстояния от точки до начала координат;
# •	метод getPoint(), который возвращает точку в виде списка;
# В подклассе PointColor реализуйте следующие атрибуты:
# •	цвет точки color;
# •	метод начальной инициализации, который получает параметры координаты точки и цвет;
# •	метод доступа к цвету color с именем getColor().
# import time
from functools import wraps
import random

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        
    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5
    
    def getPoint(self):
        return [self.x, self.y]

class PointColor(Point):
    def __init__(self, x, y, color) -> None:
        super().__init__(x, y)
        self.color = color
        
    def getColor(self):
        return self.color
    
    
    
# 5.	Напишите декоратор, оптимизирующий работу декорируемой функции. 
# Декоратор должен сохранять результат работы функции на ближайшие три запуска и вместо выполнения 
# функции возвращать сохраненный результат. После трех запусков функция должна вызываться вновь,
# а результат работы функции – вновь кешироваться. 
# Рекомендации: создайте в декоратере переменную-кеш (промежуточный буфер с быстрым доступом к нему),
# сохраните в нем результат выполнения декорируемой функции. Создайте в декораторе переменную, хранящую счетчик 
# запросов. Пока значение счетчика ниже предельного, отдавайте результат, сохраненный в кеше. Когда число запросов 
# к функции превысит предел и надо будет снова высчитывать результат выполнения функции, сбросьте счетчик, выполните 
# декорируемую функцию и заново сохраните результат ее выполнения в переменную-кеш.

# def time_deco(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Время выполнения - {end - start}")
#         return result
#     return wrapper

# @time_deco
# def calculate(a, b) -> int:
#     return a + b 


def cache_three_runs(func):
    cache = None
    counter = 0
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal cache, counter
        if cache is None or counter >= 3:
            cache = func(*args, **kwargs)
            counter = 0
        
        counter += 1
        return cache
    return wrapper


@cache_three_runs
def get_data():
    print("Функция выполняется...")
    return random.randint(1, 100)


if __name__ == '__main__':
        # Тесты для Point
    p1 = Point(3, 4)
    assert p1.distance() == 5.0, "Ошибка: расстояние вычислено неверно"
    assert p1.getPoint() == [3, 4], "Ошибка: координаты возвращаются неверно"
    print("Тесты для Point прошли успешно.")

    # Тесты для PointColor
    p2 = PointColor(6, 8, "red")
    assert p2.distance() == 10.0, "Ошибка: расстояние для PointColor вычислено неверно"
    assert p2.getPoint() == [6, 8], "Ошибка: координаты PointColor неверные"
    assert p2.getColor() == "red", "Ошибка: цвет возвращается неверно"
    print("Тесты для PointColor прошли успешно.")

    # Дополнительная проверка на другой цвет
    p3 = PointColor(0, 0, "blue")
    assert p3.distance() == 0.0, "Ошибка: расстояние до начала координат неверно"
    assert p3.getColor() == "blue", "Ошибка: цвет неверно сохраняется"
    print("Все тесты выполнены успешно")
    
    for i in range(10):
        print(i+1, "->", get_data())
    
