from typing import List
from models import Transaction
import pandas as pd
from models import Transaction, Category, TransactionType
from datetime import datetime
import matplotlib.pyplot as plt


def analyze_by_category(transactions: List[Transaction]) -> pd.DataFrame:
    """Анализ расходов/доходов по категориям"""
    df = pd.DataFrame([{
        "Amount": t.amount,
        "Category": t.category.value,
        "Type": t.type.value,
        "Date": t.date,
        "Comment": t.comment
    } for t in transactions])
    
    result = df.groupby('Category')['Amount'].sum(numeric_only=True).reset_index()
    return result

def show_plots(df: pd.DataFrame):
    """График курсов валют"""
    df.plot(figsize=(10, 5))
    plt.title("Exchange Rates Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(alpha=0.5)
    plt.legend()
    plt.show()



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
    df = analyze_by_category(transactions)
    show_plots(df)