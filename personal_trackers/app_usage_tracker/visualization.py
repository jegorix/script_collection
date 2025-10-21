import matplotlib.pyplot as plt
from analytics import Analytics
import pandas as pd
import seaborn as sns 

class Visualization:
    """Class to visualize time spend analytics"""
    
    @staticmethod
    def plot_usage_by_category(df: pd.DataFrame):
        """Show usage by category -> BarPlot"""
        data = df.groupby(df['category'])['minutes'].sum(numeric_only=True).sort_values(ascending=True)
        plt.figure(figsize=(8,5))
        sns.barplot(x=data.values, y=data.index, palette="mako")
        plt.title("App Usage by Category")
        plt.xlabel("Minutes")
        plt.ylabel("Category")
        plt.tight_layout()
        plt.show()
        
    @staticmethod
    def plot_daily_usage(df: pd.DataFrame):
        """Daily usage minutes -> Plot"""
        data = df.groupby(df["date"].dt.date)["minutes"].sum(numeric_only=True)
        plt.figure(figsize=(10,5))
        plt.plot(data.index, data.values, marker="o")
        plt.title("Daily App usage")
        plt.xlabel("Date")
        plt.ylabel("Minutes")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
    @staticmethod
    def plot_usage_by_hour(df: pd.DataFrame):
        """App usage by hour -> Plot"""
        df["day"] = df["date"].dt.day
        data = df.groupby(df["day"])["minutes"].sum(numeric_only=True)
        plt.figure(figsize=(8,4))
        plt.plot(data.index, data.values, marker="o")
        plt.title("App usage by hour")
        plt.xlabel("Hour")
        plt.ylabel("Minutes")
        plt.xticks(range(0, 24))
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
        
    @staticmethod
    def plot_last_week_trend(df: pd.DataFrame):
        """Trend of altering App usage by last 7 days"""
        last_7 = df[df["date"] >= df["date"].max() - pd.Timedelta(days=7)]
        data = last_7.groupby(df["date"].dt.date)["minutes"].sum(numeric_only=True)
        plt.figure(figsize=(8,4))
        plt.plot(data.index, data.values, marker="o")
        plt.title("Usage Trend (Last 7 days)")
        plt.xlabel("Date")
        plt.ylabel("Minutes")
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
