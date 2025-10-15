import csv
from pathlib import Path
from typing import List
from models import Transaction, Category, TransactionType
from datetime import datetime
import pandas as pd

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
        


    