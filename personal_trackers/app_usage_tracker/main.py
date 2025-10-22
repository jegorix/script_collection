from pathlib import Path
from typing import List
from datetime import datetime
from loguru import logger

from storage import (
    save_app_usage_json,
    load_app_usage_json,
    app_usage_data_to_dataframe,
    DATA_FILE,
    LOG_FILE,
    TEST_FILE
)

from analytics import Analytics
from visualization import Visualization
from models import AppUsageSchema, Category, AppUsage


def show_menu():
    print("\n=== App Usage Tracker Menu ===")
    print("1. Add App Usage Data")
    print("2. Show analtics")
    print("3. Show visualizations")
    print("4. Exit")
    print("===========================\n")



def add_app_usage_data(app_data: List[AppUsage]):
    try:
        app = input("Enter App name: ")
        category = input("Enter Category(Work, Entertainment, Social, Other): ")
        minutes = int(input("Enter minutes spent: "))
        comment = input("Enter comment")
        
        match category.capitalize():
            case "Work":
                cat = Category.WORK
            case "Entertainment":
                cat = Category.ENTERTAINMENT
            case "Social":
                cat = Category.SOCIAL
            case _:
                cat = Category.OTHER
                
        app_data_schema = AppUsageSchema(
            app=app,
            category=cat,
            minutes=minutes,
            date=datetime.now(),
            comment=comment,
        )
        
        app_data_unit = app_data_schema.to_app_usage()
        
        app_data.append(app_data_unit)
        save_app_usage_json(app_data, DATA_FILE)
        logger.success(f"App Data added {app_data_unit.to_dict()}")
        
    except Exception as e:
        logger.error(f"Error while adding App Data: {e}")
        
        
def show_analytics(app_data: List[AppUsage]):
    df = app_usage_data_to_dataframe(app_data)
    print("\n--- Analytics ---")
    print(f"Total minutes usage: {Analytics.total_usage_minutes(df)}")
    print(f"Most used App: {Analytics.most_used_app(df)}")
    print(f"Average daily usage: {Analytics.average_daily_usage(df)}")
    print(f"Weekly Trend: {Analytics.average_daily_usage(df)}")
    print(f"Extreme days stats: {Analytics.extreme_days(df)}")
    print("------------------")
    
def show_visualization(app_data: List[AppUsage]):
    df  = app_usage_data_to_dataframe(app_data)
    print("\nChoose_visualization: ")
    print("1. App Usage by Category")
    print("2. Daily Usage")
    print("3. App Usage by hour")
    print("4. Trend of altering App Usage by last 7 days")
    print("5. App Usage by category in Pie")
    print("6. Top N most using Apps")
    print("7. App Usage by week day")
    print("8. App Usage heatmap")
    print("9. Trend Behavior")
    print("10. BoxPlot for distributing inside category", end="\n\n")
    
    choice = input("Enter Option: ")
    
    match choice:
        case "1": Visualization.plot_usage_by_category(df)
        case "2": Visualization.plot_daily_usage(df)
        case "3": Visualization.plot_usage_by_hour(df)
        case "4": Visualization.plot_last_week_trend(df)
        case "5": Visualization.pie_category_usage(df)
        case "6": Visualization.bar_n_app_usage(df)
        case "7": Visualization.usage_by_day_of_week(df)
        case "8": Visualization.heatmap_usage(df)
        case "9": Visualization.usage_rolling_average(df)
        case "10": Visualization.boxplot_std_category(df)
        case _: print("Unknown Option")
        
def main():
    logger.add(LOG_FILE, format='{time} {level} {message}', level='DEBUG', rotation="1 MB", compression="zip")
    # app_data = load_app_usage_json(DATA_FILE)
    app_data = load_app_usage_json(TEST_FILE)
    
    while True:
        show_menu()
        choice = input("Choose Option: ")
        print()
        
        match choice:
            case "1":
                add_app_usage_data(app_data)
            case "2":
                show_analytics(app_data)
            case "3":
                show_visualization(app_data)
            case "4":
                print("Exit")
                break
            case _:
                print("Invalid choice, try again.")
                
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(" Work finished")
                
    

# def show_menu():
#     print("\n=== App Usage Tracker Menu ===")
#     print("1. Add App Usage Data")
#     print("2. Show analtics")
#     print("3. Show visualizations")
#     print("4. Exit")
#     print("===========================\n")