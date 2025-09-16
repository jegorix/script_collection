from typing import Any

def get_valid_choices(choices: Any) -> Any:
    choices_dict = {}
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")
        choices_dict[index] = choice
        
    
    while True:
        result = int(input("Выберите значение: "))
        try:
            result = int(result)
            return choices_dict[result]
        
        except TypeError:
            print(f"Ошибка! Введено неверное значение {result}")
            
        except Exception as e:
            print(f"Ошибка! возникла ошибка {e}")

        
if __name__ == "__main__":
    pass