from services.storage import transaction_to_dataframe, load_transaction_json
from pathlib import Path
from services.analytics import Analytics
from services.visualization import Visualization
from loguru import logger

file = Path("data/test.json")

try:
    try:
        data = load_transaction_json(file_path=file)
        df_data = transaction_to_dataframe(data)
        
        
        
    except FileNotFoundError:
        print("Файл не найден")
        
    else:  
        print(df_data, end='\n\n')
        print("Total Balance: ", Analytics.total_balance(df_data), end='\n\n')
        df_expences_by_category = Analytics.expences_by_category(df_data)
        
        logger.info(f"Expences by category: {df_expences_by_category}")
        
        # print(f"Expences by category: {df_expences_by_category}")
        Visualization.heatmap_expenses_by_day_hour(df_data)
        Visualization.scatter_expense_vs_income(df_data)
        Visualization.stacked_monthly_income_expense(df_data)
        Visualization.boxplot_expenses(df_data)
        Visualization.pie_expenses(df_data)
        Visualization.bar_expense_by_category(df_data)
        Visualization.bar_incomes_by_category(df_data)
        Visualization.plot_balance_over_time_sum(df_data)
        Visualization.bar_top_expences(df_data)
        Visualization.bar_monthly_summary(df_data)
        month_sum = Analytics.monthly_summary(df_data)
        print(month_sum)
        
except KeyboardInterrupt:
    print("Принудительное завершение")