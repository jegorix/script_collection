from typing import Dict, Any

def process_dict(data: Dict[Any,Any]) -> Dict[Any,Any]: # 41
    result = {}

    for key, value in data.items():
        try:
            processed_value = int(value)
            result[key] = processed_value ** 2 
    
        except (ValueError, TypeError):
            try:
                if len(str(value)) > 10:
                    result[key] = str(value)[:10] + '...'
                else:
                    result[key] = str(value).upper()
                    
            except (AttributeError, TypeError, Exception):
                result[key] = 'Неправильное значение'
                
    return result


class Weird:
    def __str__(self):
        raise Exception("Нельзя превратить в строку")

        
if __name__ == "__main__":
    # Тест 1. Все значения — числа (строки чисел тоже приводятся к int)
    print(process_dict({"a": 5, "b": "7", "c": -3}))  
    # ожидаем {'a': 25, 'b': 49, 'c': 9}

    # Тест 2. Строки разной длины
    print(process_dict({"short": "hi", "long": "abcdefghijklmnop"}))
    # ожидаем {'short': 'HI', 'long': 'abcdefghij...'}

    # Тест 3. Смешанные типы
    print(process_dict({"x": None, "y": [1, 2], "z": True}))
    # ожидаем {'x': 'NONE', 'y': '[1, 2]', 'z': 1} 
    # True как int = 1**2 = 1, список превращается в строку

    # Тест 4. Пустой словарь
    print(process_dict({}))
    # ожидаем {}

    # Тест 5. Значения с пробелами
    print(process_dict({"p": "   12   ", "q": "  hello world  "}))
    # ожидаем {'p': 144, 'q': 'hello wor...'}

    # Тест на "Неправильное значение"
    print(process_dict({"weird": Weird()}))
    # ожидаем {'weird': 'Неправильное значение'}