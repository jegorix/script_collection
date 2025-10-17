import pandas as pd
import numpy as np
from typing import List
from ..models.transaction import Transaction
from storage import transaction_to_dataframe

class Analytics:
    """
    Class for Transaction analytics due to pandas and numpy
    """
    
    
    @staticmethod
    def total_balance(df: pd.DataFrame) -> float:
        """
        General balance
        """
        return df['amount'].sum()
    
    
    @staticmethod
    def expences_by_category(df: pd.DataFrame) -> pd.Series:
        """
        Group Expences by category
        """
        expences = df[df['type'] == 'Expense']
        expences.groupby('category')['amount'].sum(numeric_only=True).sort_values(ascending=False)
        return expences
    
    
    @staticmethod
    def incomes_by_category(df: pd.DataFrame) -> pd.Series:
        """
        Group Incomes by category
        """
        incomes = df[df['type'] == 'Income']
        incomes.groupby('category')['amount'].sum(numeric_only=True).sort_values(ascending=False)
        return incomes
    
    
    @staticmethod
    def average_expense(df: pd.DataFrame) -> float:
        """Average amount of expense"""
        exp = df[df['type'] == 'Expense']
        return exp['amount'].mean() if not exp.empty else 0.0
    
    @staticmethod
    def average_income(df: pd.DataFrame) -> float:
        """Average amount of income"""
        inc = df[df['type'] == 'Income']
        return inc['amount'].mean() if not inc.empty else 0.0
    
    @staticmethod
    def balance_over_time(df: pd.DataFrame) -> pd.Series:
        """Dynamic balance by date"""
        df_sorted = df.sort_values("date")
        return df_sorted.groupby("date")['amount'].sum().cumsum()
    
    @staticmethod
    def top_expenses(df: pd.DataFrame, n: int = 5) -> pd.Series:
        """Top N categories by expences"""
        exp = df[df['type'] == 'Expense']
        return exp.groupby('category')['amount'].sum().nlargest(n)
    
    @staticmethod
    def monthly_summary(df: pd.DataFrame) -> pd.Series:
        """Expences and Incomes by the monthes"""
        df['month'] = df['date'].dt.to_period('M')
        summary = df.groupby(['month', 'type'])['amount'].sum().unstack(fill_value=0)
        summary['balance'] = summary.get('Income', 0) - summary.get('Expence', 0)
        return summary
    
    @staticmethod
    def expense_volatility(df: pd.DataFrame) -> float:
        """Expence Volatility"""
        exp = df[df['type'] == 'Expense']
        return exp['amount'].std() if not exp.empty else 0.0

if __name__ == '__main__':
    pass