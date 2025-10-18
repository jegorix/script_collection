import matplotlib.pyplot as plt
from .analytics import Analytics
import pandas as pd
import seaborn as sns

class Visualization:
    """Class to visualize expense plots"""
    
    @staticmethod
    def bar_expense_by_category(df: pd.DataFrame) -> None:
        exp = Analytics.expences_by_category(df)
        plt.figure(figsize=(10,8))
        plt.bar(exp.index, exp.values, color='skyblue', label='Expenses')
        plt.title("Expences by category")
        plt.xlabel("Category")
        plt.ylabel("Expences")
        plt.xticks(rotation=45)
        plt.legend()
        plt.show()
        
    @staticmethod
    def bar_incomes_by_category(df: pd.DataFrame):
        inc = Analytics.incomes_by_category(df)
        plt.figure(figsize=(10, 8))
        plt.bar(inc.index, inc.values, color='lightgreen', label='Incomes')
        plt.title("Incomes by category")
        plt.xlabel("Category")
        plt.ylabel("Incomes")
        plt.xticks(rotation=45)
        plt.legend()
        plt.show()
        
    @staticmethod
    def plot_balance_over_time_sum(df: pd.DataFrame):
        """Plot balance over time sum plot (Cumulative)"""
        balance_series = Analytics.balance_over_time(df)
        plt.figure(figsize=(10, 4))
        plt.plot(balance_series.index, balance_series.values, label="Cumulative Balance")
        plt.title("Cumulative balance")
        plt.xlabel("Date")
        plt.ylabel("Balance")
        plt.legend()
        plt.show()
        
    @staticmethod
    def bar_top_expences(df: pd.DataFrame):
        "plot top-5 categories by expences"
        exp = Analytics.top_expenses(df)
        plt.figure(figsize=(10, 4))
        plt.bar(exp.index, exp.values, color='tomato')
        plt.title("Top 5 Expense categories")
        plt.show()
        
    @staticmethod
    def bar_monthly_summary(df: pd.DataFrame):
        "bar monthly summary by expence, income and balance"
        summary = Analytics.monthly_summary(df)
        fig, ax = plt.subplots(2, 2, figsize=(12, 8))
        ax[0, 0].bar(summary.index.astype(str), summary['balance'], color='orange')
        ax[0, 0].set_title("Monthly summary by Balance")
        ax[0, 1].bar(summary.index.astype(str), summary['Income'], color='green')
        ax[0, 1].set_title("Monthly summary by Income")
        ax[1, 0].bar(summary.index.astype(str), summary['Expense'], color='red')
        ax[1, 0].set_title("Monthly summary by Expense")
        plt.suptitle("Monthly summary by expense, income and balance")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    @staticmethod
    def pie_expenses(df: pd.DataFrame):
        """Pie diagram Expenses by category"""
        exp = Analytics.expences_by_category(df)
        exp = exp.abs()
        plt.figure(figsize=(8,8))
        plt.pie(exp.values, labels=exp.index, autopct="%1.1f%%", startangle=90)
        plt.title("Expense distribution by category")
        plt.show()

    
    @staticmethod
    def boxplot_expenses(df: pd.DataFrame):
        """Boxplot for expenses distribution analytics"""
        exp = df[df['type'] == 'Expense']
        if not exp.empty:
            plt.figure(figsize=(6,6))
            sns.boxplot(y=exp['amount'], color='lightblue')
            plt.title("Expense distribution (Boxplot)")
            plt.ylabel("Amount")
            plt.show()
            

    @staticmethod
    def stacked_monthly_income_expense(df: pd.DataFrame):
        """Stacked bar: expenses and incomes by monthes"""
        summary = Analytics.monthly_summary(df)
        
        summary[['Income', 'Expense']].plot(
            kind='bar', stacked=True, figsize=(10, 6), color=['pink', 'lightblue']
        )
        
        plt.title("Income and Expense by Month")
        plt.xlabel("Month")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)
        plt.legend()
        plt.show()
        
    

if __name__ == '__main__':
    pass