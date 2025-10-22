import matplotlib.pyplot as plt
from analytics import Analytics
import pandas as pd
import seaborn as sns 

order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

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
        
    @staticmethod
    def pie_category_usage(df: pd.DataFrame):
        """Show usage by category represented in pie chart"""
        data = df.groupby(df["category"])["minutes"].sum(numeric_only=True).sort_values(ascending=False)
        plt.figure(figsize=(8,5))
        plt.pie(data.values, labels=data.index, autopct="%1.1f%%", startangle=140)
        plt.title("Minutes distribution by category")
        plt.show()
        
    
    @staticmethod
    def bar_n_app_usage(df: pd.DataFrame, n: int = 10):
        """Show top N using Apps"""
        data = df.groupby(df["app"])["minutes"].sum(numeric_only=True).sort_values(ascending=False).head(n)
        plt.figure(figsize=(8,5))
        sns.barplot(y=data.index, x=data.values, palette="viridis")
        plt.xlabel("Minutes")
        plt.ylabel("Application")
        plt.suptitle(f"Top {n} using Apps")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show() 
        
        
    @staticmethod
    def usage_by_day_of_week(df: pd.DataFrame):
        """App usage by week of day"""
        df['weekday'] = df['date'].dt.day_name()
        data = df.groupby(df["weekday"])["minutes"].sum(numeric_only=True)
        plt.figure(figsize=(8,5))
        plt.bar(order, data.values, color="orange")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
    @staticmethod
    def heatmap_usage(df: pd.DataFrame):
        """Show maximum usage based on week day and hour"""
        df['weekday'] = df['date'].dt.day_name()
        df['hour'] = df['date'].dt.hour
        plt.figure(figsize=(10, 6))
        
        pivot = df.pivot_table(
            values='minutes',
            index='weekday',
            columns='hour',
            aggfunc='sum',
        )
        
        # TO USE AN ORDER
        pivot = pivot.reindex(order)
        
        
        sns.heatmap(pivot, cmap='mako', linewidths=.5)
        plt.title("Heatmap usage by weekday and hour")
        plt.xlabel("Hour of Day")
        plt.ylabel("Day of Week")
        plt.show()
        
        
    @staticmethod
    def usage_rolling_average(df: pd.DataFrame):
        """Show main Trend raise or decline"""
        data = df.groupby(df['date'].dt.date)['minutes'].sum(numeric_only=True)
        plt.figure(figsize=(8, 5))
        data_rol = data.rolling(window=7).mean(numeric_only=True)
        plt.plot(data.index, data.values, color='blue')
        plt.plot(data_rol.index, data_rol.values, color='red')
        plt.title("Show main Trand using rolling average")
        plt.grid(True, alpha=0.3)
        plt.show()
        
    @staticmethod
    def boxplot_std_category(df: pd.DataFrame):
        """Boxplot for distributing inside category"""
        plt.figure(figsize=(8,5))
        sns.boxplot(x='category', y='minutes', data=df, palette="Set2")
        plt.yscale('log')
        plt.title('Distributing inside categories')
        plt.xlabel('Category')
        plt.ylabel('Minutes')
        plt.show()
        