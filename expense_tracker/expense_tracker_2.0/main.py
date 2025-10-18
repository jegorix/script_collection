from pathlib import Path
from typing import List
from datetime import datetime
from loguru import logger

from services.storage import (
    load_transaction_json,
    save_transactions_json,
    transaction_to_dataframe
)

from services.analytics import Analytics
from services.visualization import Visualization
from models.transaction import TransactionSchema, Category, TransactionType


DATA_FILE = Path("data/data.json")

def print_menu() -> None:
    print("\n=== Expense Tracker Menu ===")
    print("1. Add transaction")
    print("2. Show total balance")
    print("3. Show analtics")
    print("4. Show visualizations")
    print("5. Exit")
    print("===========================\n")
    
    
def add_transaction(transactions: List[Transaction]) -> None:
    try:
        amount = float(input("Enter amount: "))
        category = input("Enter Category(Food, Transport, Rent, Salary, Other): ")
        type_input = input("Type (Income/Expense): ")
        user_comment = input("Enter comment: ")
        
        match category.capitalize():
            case "Food":
                cat = Category.FOOD
            case "Transport":
                cat = Category.TRANSPORT
            case "Rent":
                cat = Category.RENT
            case "Salary":
                cat = Category.SALARY
            case _:
                cat = Category.OTHER
                
        match type_input.capitalize():
            case "Income":
                ttype = TransactionType.INCOME
            case "Expense":
                ttype = TransactionType.EXPENSE
            case _:
                print("Invalid type, default EXPENSE")
                ttype = TransactionType.EXPENSE
                
        transaction_shema = TransactionSchema(
            amount=abs(amount) if ttype == TransactionType.INCOME else -abs(amount),
            category=cat,
            type=ttype,
            date=datetime.now(),
            comment=user_comment
        )
        transaction = transaction_shema.to_transaction()
        
        transactions.append(transaction)
        save_transactions_json(transactions, DATA_FILE)
        logger.success(f"Transaction added {transaction.to_dict()}")
        
    except Exception as e:
        logger.error(f"Error while adding transaction: {e}")
        
    
def show_analytics(transactions: List[Transaction]) -> None:
    df = transaction_to_dataframe(transactions)
    print("\n--- Analytics ---")
    print(f"Total Balance: {Analytics.total_balance(df):.2f}")
    print(f"Average Expense: {Analytics.average_expense(df):.2f}")
    print(f"Average Income: {Analytics.average_income(df):.2f}")
    print(f"Expense Volatility: {Analytics.expense_volatility(df):.2f}")
    print("------------------")
    

def show_visualizations(transactions: List[Transaction]) -> None:
    df = transaction_to_dataframe(transactions)
    
    print("\nChoose visualization:")
    print("1. Expenses by category")
    print("2. Incomes by category")
    print("3. Balance over time")
    print("4. Top expenses")
    print("5. Monthly summary")
    print("6. Pie chart expenses")
    print("7. Boxplot expenses")
    print("8. Stacked income vs expense")
    print("9. Scatter income vs expense")
    print("10. Heatmap expenses by day/hour", end='\n\n')
    
    choice = input("Enter Option: ")
    
    match choice:
        case "1": Visualization.bar_expense_by_category(df)
        case "2": Visualization.bar_incomes_by_category(df)
        case "3": Visualization.plot_balance_over_time_sum(df)
        case "4": Visualization.bar_top_expences(df)
        case "5": Visualization.bar_monthly_summary(df)
        case "6": Visualization.pie_expenses(df)
        case "7": Visualization.boxplot_expenses(df)
        case "8": Visualization.stacked_monthly_income_expense(df)
        case "9": Visualization.scatter_expense_vs_income(df)
        case "10": Visualization.heatmap_expenses_by_day_hour(df)
        case _: print("Unknown Option")
        
def main() -> None:
    logger.add("logs/app.log",format='{time} {level} {message}', level='DEBUG', rotation="1 MB", compression="zip")
    transactions = load_transaction_json(DATA_FILE)
    
    while True:
        print_menu()
        choice = input("Choose option: ")
        print("\n")
        
        match choice:
            case "1":
                add_transaction(transactions)
            case "2":
                df = transaction_to_dataframe(transactions)
                print(f"Total Balance: {Analytics.total_balance(df):.2f}")
            case "3":
                show_analytics(transactions)
            case "4":
                show_visualizations(transactions)
            case "5":
                print("Bye!")
                break
            case _:
                print("Invalid choice, try again.")
                    
                    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(" Завершение программы!")