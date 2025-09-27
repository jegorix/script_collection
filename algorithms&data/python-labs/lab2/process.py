from typing import Any, Union, List

def process_data(data: Any) -> Union[int, float, str, List]:
    try:
        if isinstance(data, (int, float)):
            return f"Новое число = {data * 2}"
        
        elif isinstance(data, str):
            try:
                number = float(data)
                print(f"Строка преобразована в число: {number}")
                return number
            
            except TypeError:
                return f"Строка преобразована {data.upper()}"
                
        elif isinstance(data, list):
            if len(data) == 0:
                raise ValueError("Передан пустой список")
            
            try:
                average = sum(data) / len(data)
                print(f"Среднее значение списка: {average}")
                return average
            except TypeError:
                result = len(data)
                print(f"Длина списка: {result}")
                return result
        else:
            raise TypeError(f"Неподдерживаемый тип данных: {type(data).__name__}")
        
        
    except ValueError as e:
        return f"ValueError: {e}"
    
    except TypeError as e:
        return f"TypeError: {e}"
    
    except ZeroDivisionError:
        return "ZeroDivisionError: Деление на ноль невозможно"
    
    except Exception as e:
        return f"UnexpectedError: {e}"
    
    
if __name__ == "__main__":
    # Тест 1. Целое число
    print(process_data(10))  # ожидаем "Новое число = 20"

    # Тест 2. Вещественное число
    print(process_data(3.5))  # ожидаем "Новое число = 7.0"

    # Тест 3. Строка, которая является числом
    print(process_data("42"))  # ожидаем 42.0 и вывод "Строка преобразована в число: 42.0"

    # Тест 4. Строка, не являющаяся числом
    print(process_data("hello"))  # ожидаем "hello" (вверх регистр, если код TypeError не сработает, иначе просто строка)

    # Тест 5. Пустой список
    print(process_data([]))  # ожидаем "ValueError: Передан пустой список"

    # Тест 6. Список чисел
    print(process_data([1, 2, 3, 4]))  # ожидаем 2.5 и вывод "Среднее значение списка: 2.5"

    # Тест 7. Список с нечисловыми элементами
    print(process_data([1, "a", 3]))  # ожидаем 3 (длина списка) и вывод "Длина списка: 3"

    # Тест 8. Неизвестный тип
    print(process_data({"a": 1}))  # ожидаем "TypeError: Неподдерживаемый тип данных: dict"