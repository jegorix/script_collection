import pandas as pd
from typing import Dict
from models import AppUsage

class Analytics:
    """Class for App Usage Data analytics through pandas and numpy"""
    
    @staticmethod
    def format_minutes(minutes: int) -> str:
        result = f"{minutes} min" if minutes < 60 else f"{round(minutes / 60, 2)} h"
        return result
    
    @staticmethod
    def total_usage_minutes(df: pd.DataFrame) -> str:
        """Total usage minutes"""
        return Analytics.format_minutes(int(df['minutes'].sum()))
    
    @staticmethod
    def usage_by_category(df: pd.DataFrame) -> pd.Series:
        """Group category by minutes"""
        series = df.groupby(df['category'].astype(str))['minutes'].sum(numeric_only=True).sort_values(ascending=False)
        return series.apply(Analytics.format_minutes)
    
    @staticmethod
    def most_used_app(df: pd.DataFrame) -> str:
        """Name of the most used app"""
        return str(df.loc[df['minutes'].idxmax(), 'app'])
    
    @staticmethod
    def daily_usage(df: pd.DataFrame) -> pd.Series:
        """Daily usage (group by date only)"""
        data_series = df.groupby(df["date"].dt.date)["minutes"].sum(numeric_only=True)
        return data_series.apply(Analytics.format_minutes)
    
    @staticmethod
    def average_daily_usage(df: pd.DataFrame) -> str:
        """Average Daily Usage"""
        daily = df.groupby(df["date"].dt.date)["minutes"].sum()
        avg = int(daily.mean())
        return Analytics.format_minutes(avg)
    
    @staticmethod
    def average_month_usage(df: pd.DataFrame) -> pd.Series:
        """Average Usage per month"""
        series = df.groupby(df["date"].dt.month)["minutes"].mean(numeric_only=True)
        
        return series.apply(Analytics.format_minutes)
    
    @staticmethod
    def top_n_apps(df: pd.DataFrame, n: int = 5) -> pd.Series:
        seris = df.groupby(df["app"])["minutes"].sum(numeric_only=True).nlargest(n)
        return seris.apply(Analytics.format_minutes)
    
    @staticmethod
    def weekly_trend(df: pd.DataFrame) -> str:
        last_week = df[df["date"] >= (df["date"].max() - pd.Timedelta(days=7))]
        prev_week = df[(df["date"] < (df["date"].max() - pd.Timedelta(days=7))) &
                       (df["date"] >= (df["date"].max() - pd.Timedelta(days=14)))]
        
        last_week_avg = last_week['minutes'].mean()
        prev_week_avg = prev_week['minutes'].mean()
        
        if pd.isna(prev_week_avg) or prev_week_avg == 0:
            return "Not enough data"
        
        diff = ((last_week_avg - prev_week_avg) / prev_week_avg) * 100
        trend = "↑ Growth" if diff > 0 else "↓ Decline"
        return f"{trend} ({diff:.2f}%)"
    
    @staticmethod
    def usage_by_hour(df: pd.DataFrame) -> pd.Series:
        df["hour"] = df["date"].dt.hour
        series = df.groupby("hour")["minutes"].sum(numeric_only=True)
        return series.sort_index()
    
    @staticmethod
    def category_precentage(df: pd.DataFrame) -> pd.Series:
        total = df["minutes"].sum()
        result = (df.groupby(df["category"])["minutes"].sum(numeric_only=True) / total) * 100
        return result.round(2).sort_values(ascending=False)
    
    @staticmethod
    def extreme_days(df: pd.DataFrame) -> Dict[str, str]:
        daily = df.groupby(df['date'].dt.date)['minutes'].sum()
        most_active = daily.idxmax()
        least_active = daily.idxmin()
        return {
            "most_active_day": str(most_active),
            "least_active_day": str(least_active),
            "max_minutes": Analytics.format_minutes(int(daily.max())),
            "min_minutes": Analytics.format_minutes(int(daily.min()))
        }
        
    
    
if __name__ == '__main__':
    pass
