from typing import Union

def multiply(a,b: Union[int, float]) -> Union[int, float]:
    return a*b


if __name__ == "__main__":
    # Тест 1. Целые числа
    print(multiply(2, 3))          # ожидаем 6

    # Тест 2. Целое и float
    print(multiply(2, 3.5))        # ожидаем 7.0

    # Тест 3. Два float
    print(multiply(2.5, 4.0))      # ожидаем 10.0

    # Тест 4. Отрицательные числа
    print(multiply(-3, 5))         # ожидаем -15

    # Тест 5. Умножение на ноль
    print(multiply(0, 99))         # ожидаем 0