
from typing import List

def process_numbers(numbers_list: List[int|float]) -> List[int|float]:
    new_arr = []
    for number in numbers_list:
        try:
            valid_number = int(number) if number.is_integer() else float(number)
            new_arr.append(valid_number**2)
            
        except TypeError:
            print(f"Ошибка! {number} не является числом!")
            
        
        except Exception as e:
            print(f"Ошибка! возникла ошибка {e}")
        
    return new_arr
        
        
if __name__ == "__main__":
    
    """
    33. Создайте функцию `process_numbers(numbers)`, 
    которая обрабатывает список чисел и использует
    исключения для обработки некорректных данных.
    """
    
    print(process_numbers([1, 2, 3]))  # ожидаем [1, 4, 9]

    print("\nTest 2. Целые + вещественные")
    print(process_numbers([1.0, 2.5, 3]))  # ожидаем [1, 6.25, 9]

    print("\nTest 3. Смешанные типы (есть строка)")
    print(process_numbers([23, 43, '23', 6]))  # '23' вызовет сообщение об ошибке

    print("\nTest 4. Пустой список")
    print(process_numbers([]))  # ожидаем []

    print("\nTest 5. Некорректные типы (список, словарь)")
    print(process_numbers([1, [2, 3], {'a': 1}]))  # список и словарь вызовут ошибку

            