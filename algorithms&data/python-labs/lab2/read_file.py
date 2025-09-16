
def read_lines(filename: str):
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
        
    except FileNotFoundError:
        print(f"Ошибка! Файл '{filename}' не найден")
        return None
    
    except PermissionError:
        print(f"Ошибка! Нет прав на чтение файла '{filename}'")
        return None
    
    except Exception as e:
        print(f"Неожиданная ошибка при чтении файла '{filename}': {e}")
        return None
    
        
        