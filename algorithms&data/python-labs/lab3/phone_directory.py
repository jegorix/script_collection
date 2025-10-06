import json
from pprint import pprint
from typing import List, Dict
import re

phonebook_file = 'lab3/files/phonebook.json'

phonebook = {
    "contacts": [
        {"first_name": "Адриан", "last_name": "Григорцевич", "phone": "+375291234567"},
        {"first_name": "Мария", "last_name": "Иванова", "phone": "+375293456789"},
        {"first_name": "Алексей", "last_name": "Петров", "phone": "+375297654321"},
        {"first_name": "Ольга", "last_name": "Сидорова", "phone": "+375299876543"},
        {"first_name": "Дмитрий", "last_name": "Кузнецов", "phone": "+375291112233"},
        {"first_name": "Анна", "last_name": "Федорова", "phone": "+375295554433"},
        {"first_name": "Иван", "last_name": "Смирнов", "phone": "+375296667788"},
        {"first_name": "Елена", "last_name": "Морозова", "phone": "+375292223344"},
        {"first_name": "Сергей", "last_name": "Васильев", "phone": "+375293334455"},
        {"first_name": "Наталья", "last_name": "Лебедева", "phone": "+375297778899"}
    ]
}


def create_json(filename: str, data: Dict) -> None:
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Файл {filename} обновлен.")


def load_contacts(filename: str) -> List[Dict]:
    try:
        with open(filename, mode='r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get("contacts", [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise Exception("Файл поврежден или не является JSON.")


def input_number() -> str:
    while True:
        number = input("Введите номер телефона (+375XXXXXXXXX): ").strip()
        if re.fullmatch(r'\+375\d{9}', number):
            return number
        print("Неверный формат номера! Пример правильного: +375291234567")


def input_name() -> str:
    while True:
        name = input("Введите имя или фамилию для поиска: ").strip()
        if name:
            return name
        print("Поле не может быть пустым. Попробуйте снова.")


def input_contact() -> Dict:
    first_name = input("Введите имя: ").strip()
    last_name = input("Введите фамилию: ").strip()
    phone = input_number()
    return {"first_name": first_name, "last_name": last_name, "phone": phone}


def add_contact(filename: str) -> None:
    contacts = load_contacts(filename)
    data = input_contact()
    contacts.append(data)
    create_json(filename, {"contacts": contacts})
    print(f"{data} - запись успешно добавлена в контакты.")


def find_contacts_by_name(filename: str) -> None:
    contacts = load_contacts(filename)
    name = input_name()
    results = [c for c in contacts if name.lower() in c['first_name'].lower() or name.lower() in c['last_name'].lower()]
    if results:
        print("Найденные контакты:")
        for c in results:
            print(f"{c['first_name']} {c['last_name']} - {c['phone']}")
    else:
        print("Контакты не найдены.")


def find_contacts_by_phone_number(filename: str) -> None:
    contacts = load_contacts(filename)
    number = input_number()
    results = [c for c in contacts if number == c['phone']]
    if results:
        print("Найденные контакты:")
        for c in results:
            print(f"{c['first_name']} {c['last_name']} - {c['phone']}")
    else:
        print("Контакты не найдены.")


def show_contacts_info(filename: str) -> None:
    contacts = load_contacts(filename)
    if contacts:
        print("Список всех контактов:")
        for c in contacts:
            print(f"{c['first_name']} {c['last_name']} - {c['phone']}")
    else:
        print("Справочник пуст.")


def menu(filename: str):
    while True:
        print("""
Выберите действие:
1. Загрузить информацию из справочника.
2. Добавить контакт.
3. Выполнить поиск контактов по имени.
4. Выполнить поиск контактов по номеру телефона.
5. Выход.
""")
        try:
            num = int(input('>> '))
        except ValueError:
            print("Неверный выбор! Выберите число от 1 до 5")
            continue

        match num:
            case 1:
                show_contacts_info(filename)
            case 2:
                add_contact(filename)
            case 3:
                find_contacts_by_name(filename)
            case 4:
                find_contacts_by_phone_number(filename)
            case 5:
                print("Выход...")
                break
            case _:
                print("Неверный выбор! Попробуйте снова.")


if __name__ == '__main__':
    create_json(phonebook_file, phonebook)
    menu(phonebook_file)