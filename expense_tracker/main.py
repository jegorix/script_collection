from models import Transaction, Category, TransactionType
from datetime import date

transactions = []

def add_transaction():
    amount = float(input("Сумма: "))
    category = Category[input("Категория (FOOD, TRANSPORT, RENT, SALARY, OTHER): ").upper()]
    t_type = TransactionType[input("Тип (INCOME/EXPENSE): ").upper()]
    t_date = date.fromisoformat(input("Дата (YYYY-MM-DD): "))
    comment = input("Комментарий (необязательно): ")
    
    transaction = Transaction(amount=amount, category=category, type=t_type, date=t_date, comment=comment)
    transactions.append(transaction)
    print("Транзакция добавлена!")
    
def show_transactions():
    for t in transactions:
        print(t)
        
def main_menu():
    
    while True:
        print("\nМеню:")
        print("1. Добавить транзакцию")
        print("2. Показать транзакции")
        print("3. Выход")
        choice = input("Выберите действие: ")
        
        match choice.strip().lower():
            case "1":
                add_transaction()
            case "2":
                show_transactions()
            case "3":
                break
            case _:
                print("Некорректный выбор!")
        
if __name__ == '__main__':
    main_menu()
    