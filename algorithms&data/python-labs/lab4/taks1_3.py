# 1.	Напишите программу, создающую класс MinVoda (
    # для определения типа минеральной воды), принимающую один аргумент при инициализации 
    # (отвечающий за тип выбираемой минеральной воды: столовая или лечебная). 
# В этом классе реализуется метод show_my_drink () и на печать выводится фраза «Минеральная вода
# – {Тип минеральной воды}» при указании типа минеральной воды. В противном случае на печать выводится фраза 
# «Обычная минеральная вода».
# from abc import ABC, abstractmethod
from typing import Optional

class MinVoda():
    def __init__(self, my_drink: Optional[str] = None) -> None:
        self.my_drink = my_drink 
    
    def show_my_drink(self):
        message = f"Минеральная вода – {self.my_drink}" if self.my_drink is not None else "Обычная минеральная вода"
        print(message)
        
# 2.	Напишите программу, которая создает класс Triangle (представляющий собой треугольник).
# Конструктор этого класса должен принимать на вход три числа (длины сторон треугольника), 
# также у этого класса должен быть метод, возвращающий периметр. 
# Надо наследовать класс EquilateralTriangle, 
# представляющий равносторонний треугольник от класса Triangle. 
# Переопределить конструктор этого класса с использованием конструктора базового класса.
# Конструктор класса EquilateralTriangle должен принимать на вход одно число (длину стороны). 
# Программа должна возвращать следующие значения в зависимости от ситуации:

# •	Можно построить треугольник!;
# •	Это равносторонний треугольник!;
# •	Периметр треугольника равен = ;
# •	Треугольник не сделать из этого.

class EquilateralTriangle():
    def __init__(self, a: int) -> None:
        self.a = a

class Triangle(EquilateralTriangle):
    def __init__(self, a: int, b: int, c: int) -> None:
        super().__init__(a)
        self.b = b
        self.c = c
        
    @property
    def check_equality(self) -> str:
        return "Это равносторонний треугольник!" if (self.a == self.b == self.c) else "Это не равносторонний треугольник!"
    
    @property
    def perimeter(self) -> str:
        return f"Периметр треугольника равен = {round((self.a + self.b + self.c) / 3, 2)}"
    
    @property
    def can_be_triangle(self) -> str:
        sides = [self.a, self.b, self.c]
        max_side = max(sides)
        if max_side >= sum(sides) - max_side:
            return "Треугольник не сделать из этого."
        return "Можно построить треугольник!"
    
# 3.	Напишите программу, реализующую перегрузку оператора + для класса Point, 
# который реализует точку на плоскости. В классе должны быть реализованы следующие методы:
# •	_init_(),который перегружает конструктор класса. Конструктор класса вызывается при создании экземпляра класса;
# •	getXY(), который возвращает значение координат точки (х;у) в виде списка;
# •	_add_(),который реализует перегрузку оператора сложения.
# Реализация предусматривает суммирование координат по осям Х и У;
# •	Show(), который выводит координаты точки на экран.

    
class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y    
    
    def getXY(self):
        return [self.x, self.y]
        
    def __add__(self, obj):
        return (self.x + obj.x, self.y + obj.y)
    
    def show(self) -> None:
        print(f"Point({self.x}, {self.y})")
    
    
if __name__ == "__main__":
    # Tests for MinVoda
    water_mineral = MinVoda("Лечебная")
    water_mineral.show_my_drink()
    water_still = MinVoda()
    water_still.show_my_drink()
    
    # Tests for Triangle
    triangle_1 = Triangle(5, 9, 12)
    print(triangle_1.can_be_triangle)
    print(triangle_1.perimeter)
    print(triangle_1.check_equality)
    
    # Tests for Point
    point1 = Point(4, 7)
    point2 = Point(6, 3)
    print(point1.getXY())
    point1.show()
    print(point1 + point2)
    
