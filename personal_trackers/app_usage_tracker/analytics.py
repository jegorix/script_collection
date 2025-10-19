import pandas as pd
from typing import List
from models import AppUsage

class Analytics:
    """Class for App Usage Data analytics through pandas and numpy"""
    
    @staticmethod
    def total_usage_minutes(df: pd.DataFrame) -> int:
        """Total usage minutes"""
        return df['minutes'].sum()
    
    @staticmethod
    def usage_by_category(df: pd.DataFrame) -> pd.Series:
        """Group category by minutes"""
        return df.groupby('category')['minutes'].sum(numeric_only=True).sort_values(ascending=False)
    
    @staticmethod
    def most_used_app(df: pd.DataFrame) -> str:
        series = df.loc[df['minutes'].idxmax(), 'app']
        return str(series)
    
    
if __name__ == '__main__':
    pass
