
def get_positive_integer() -> int | float:
    print("Введите положительное число: ")
    while True:
        try:
            num = float(input())
        except Exception:
            print("Нечисловое значение. Повторите ввод!")
            continue
        if num < 0:
            print("Число отрицательное. Повторите ввод!")
            continue
        return num
        

# def get_positive_integer() -> int | float:
#     print("Введите положительное число: ")
#     while True:
#         try:
#             num = float(input())
#         except Exception:
#             raise TypeError("Ошибка! Введено нечисловое значение!")
#         if num < 0:
#             raise ValueError("Ошибка! Введено отрицательное значение!")
#         return num
        