
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
    
    
if __name__ == "__main__":
    # Тест 1. Файл существует, содержит несколько строк
    print(read_lines("files/example.txt"))  
    # ожидаем список строк без переносов, например ["строка1", "строка2", "строка3"]

    # Тест 2. Файл не существует
    print(read_lines("files/nonexistent.txt"))  
    # ожидаем None и вывод "Ошибка! Файл 'nonexistent.txt' не найден"

    # Тест 3. Файл существует, но нет прав на чтение
    # Для теста можно временно убрать права: chmod a-r files/secret.txt
    print(read_lines("files/secret.txt"))  

    # Тест 4. Пустой файл
    print(read_lines("files/empty.txt"))  
    # ожидаем [] (пустой список)
        