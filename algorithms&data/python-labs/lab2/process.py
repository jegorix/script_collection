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