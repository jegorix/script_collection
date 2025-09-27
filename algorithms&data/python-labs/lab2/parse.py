from typing import Optional

def parse_number(value: str) -> Optional[int | float]:
    
    try:
        return int(value)
    except ValueError:
        
        try:
            return float(value)
        except ValueError:
            return None
            
    
if __name__ == "__main__":
    # Тест 1. Целое число
    print(parse_number("42"))           # ожидаем 42

    # Тест 2. Вещественное число
    print(parse_number("3.14"))         # ожидаем 3.14

    # Тест 3. Отрицательное число
    print(parse_number("-7"))           # ожидаем -7

    # Тест 4. Строка не число
    print(parse_number("abc"))          # ожидаем None

    # Тест 5. Пустая строка
    print(parse_number(""))             # ожидаем None

    # Тест 6. Число с пробелами
    print(parse_number("   15   "))     # ожидаем 15

    # Тест 7. Научная нотация
    print(parse_number("1e3"))          # ожидаем 1000.0