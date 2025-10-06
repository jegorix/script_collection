# Создайте текстовый файл, в котором хранится информация
# о занятости мест в зрительном зале в двоичном виде (0 – свободно, 1 – занято).
# Количество рядов рассчитывается по формуле: 
# возраст одного из родителей минус возраст студента. 
# Количество мест в ряду – 15.  

# Напишите программу, 
# которая позволит пользователю увидеть количество свободных мест, 
# а также, введя номер ряда и места, получить информацию, свободно или занято место.
# в зале будет 26 рядов по 15 мест.

from typing import List, Optional

def _get_data_places(filename: str) ->  Optional[List[str]]:
    try:
        with open(filename, encoding='utf-8', mode='r') as f:
            return f.readlines()
    except (FileExistsError, FileNotFoundError) as e:
        raise Exception(f"Возникла проблема с файлом: {e}")

    except Exception as e:
        raise Exception(f"Возникла ошибка: {e}")
    
    
def _process_data_places(filename: str) -> List[int]:
    lines = [line.strip('\n') for line in _get_data_places(filename)]
    array_places = []
    for line in lines:
        for num in line:
            try:
                array_places.append(int(num))
            except TypeError:
                raise Exception("Неверное значение для места")
    return array_places
                

def get_free_places(filename: str):
    array_places = _process_data_places(filename)
    return len(array_places)

def check_place(filename: str):
    array_places = _process_data_places(filename)
    rows = 26
    seats_per_row = 15
    
    try:
        row = int(input("Введите номер ряда (1-26): "))
        seat = int(input("Введите номер места (1-15): "))
    except ValueError:
        print("Некорректный ввод! Нужно число.")
        return
    
    if not (1 <= row <= rows) or not (1 <= seat <= seats_per_row):
        print("Ряд или место вне допустимого диапазона.")
        return
    
    index = (row-1) * seats_per_row + (seat-1)
    
    status = "Занято" if array_places[index] == 1 else "Свободно"
    print(f"Ряд {row}, Место {seat}: {status}")


def menu(filename: str):
    while True:
        print("""
              Выберите действие:
              1. Количество свободных мест.
              2. Введите номер ряда(1-26) и место(1-15)
              3. Выход
              """)
        try:
            num = int(input('>> '))
        except (TypeError, ValueError):
            print("Неверный выбор! Выберите число от 1 до 3")
        
        match num:
            case 1:
                array_places = _process_data_places(filename)
                free_count = array_places.count(0)
                print(f"Количество свободных мест: {free_count}")
            case 2:
                check_place(filename)
            case 3:
                return 'Выход...'
                
    
if __name__ == '__main__':
    
    print(menu('lab3/files/cinema.txt'))