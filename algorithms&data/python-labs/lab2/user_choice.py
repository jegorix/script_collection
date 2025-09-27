from typing import Any

def get_valid_choices(choices: list[str]) -> Any:

    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    while True:
        user_input = input("Выберите значение: ")
        try:
            num = int(user_input)
            if 1 <= num <= len(choices):
                return choices[num - 1]
            else:
                print(f"Ошибка! Число должно быть от 1 до {len(choices)}")
        except ValueError:
            print(f"Ошибка! '{user_input}' не является числом")


if __name__ == "__main__":
    fruits = ["Яблоко", "Груша", "Банан"]
    choice = get_valid_choices(fruits)
    print(f"Вы выбрали: {choice}")