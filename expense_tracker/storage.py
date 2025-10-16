import csv
from pathlib import Path
from typing import List
from models import Transaction, Category, TransactionType
from datetime import datetime
import pandas as pd

transactions = []

DATA_FILE = Path("transactions.csv")

def save_transactions(transactions: List[Transaction]):
    """Save list of transactions to CSV file"""
    with open(DATA_FILE, mode='w', newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["amount", "category", "type", "date", "comment"])
        for t in transactions:
            writer.writerow(t.amount, t.category.value, t.type.value, t.date.isoformat(), t.comment)
            
            
def load_transaction() -> List[Transaction]:
    """Load transactions from CSV"""
    transactions: List[Transaction] = []
    
    if not DATA_FILE.exists():
        return transactions
    
    with open(DATA_FILE, mode='r', encoding='UTF-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            transactions.append(
                Transaction(
                    amount=float(row['amount']),
                    category=Category(row['category']),
                    type=TransactionType(row['type']),
                    date=datetime.fromisoformat(row['date']),
                    comment=row['comment']
                )
            )
    
    return transactions


def export_to_excel(transactions: List[Transaction], filename: str = "transcations.xlsx"):
    """Export to Excel with Pandas"""
    df = pd.DataFrame([{
        "Amount": t.amount,
        "Category": t.category.value,
        "Type": t.type.value, 
        "Date": t.date,
        "Comment": t.comment
    } for t in transactions ])
    df.to_excel(filename, index=False)
    
    
        
        
if __name__ == '__main__':
    transactions = [
        Transaction(-15.5, Category.FOOD, TransactionType.EXPENSE, datetime(2024, 1, 3), "Обед в кафе"),
        Transaction(-50.0, Category.TRANSPORT, TransactionType.EXPENSE, datetime(2024, 1, 5), "Проездной на месяц"),
        Transaction(-300.0, Category.RENT, TransactionType.EXPENSE, datetime(2024, 1, 6), "Аренда квартиры"),
        Transaction(1000.0, Category.SALARY, TransactionType.INCOME, datetime(2024, 1, 10), "Зарплата"),
        Transaction(-25.0, Category.FOOD, TransactionType.EXPENSE, datetime(2024, 1, 12), "Продукты"),
        Transaction(-10.0, Category.OTHER, TransactionType.EXPENSE, datetime(2024, 1, 15), "Подписка Netflix"),
        Transaction(-35.0, Category.TRANSPORT, TransactionType.EXPENSE, datetime(2024, 1, 18), "Такси"),
        Transaction(-120.0, Category.FOOD, TransactionType.EXPENSE, datetime(2024, 1, 20), "Ужин в ресторане"),
        Transaction(200.0, Category.OTHER, TransactionType.INCOME, datetime(2024, 1, 22), "Фриланс"),
        Transaction(-80.0, Category.RENT, TransactionType.EXPENSE, datetime(2024, 1, 25), "Коммунальные услуги"),
    ]
        


    