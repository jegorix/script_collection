from datetime import datetime
from models import Category
from storage import load_app_usage_json, TEST_FILE, app_usage_data_to_dataframe
from analytics import Analytics
from visualization import Visualization

#     schema = AppUsageSchema(
#     app='Telegram',
#     category=Category("Social"),
#     minutes=20,
#     date=datetime.now(),
#     comment="Some comment"
# )
#     transaction = schema.to_app_usage()
#     save_app_usage_json([transaction])
try:
    data = load_app_usage_json(TEST_FILE)
    # print(data)
    df_data = app_usage_data_to_dataframe(data)
    print(df_data, end="\n\n")
    print(Analytics.total_usage_minutes(df_data))
    print(Analytics.most_used_app(df_data))
    print(Analytics.daily_usage(df_data).head(3), end='\n\n')
    print(Analytics.average_daily_usage(df_data))
    # print(Analytics.average_month_usage(df_data))
    print(Analytics.top_n_apps(df_data))
    print(Analytics.weekly_trend(df_data))
    print(Analytics.category_precentage(df_data))

    Visualization.boxplot_std_category(df_data)
    Visualization.usage_rolling_average(df_data)
    Visualization.heatmap_usage(df_data)
    Visualization.usage_by_day_of_week(df_data)
    Visualization.bar_n_app_usage(df_data)
    Visualization.pie_category_usage(df_data)
    Visualization.plot_usage_by_category(df_data)
    Visualization.plot_daily_usage(df_data)
    Visualization.plot_usage_by_hour(df_data)
    Visualization.plot_last_week_trend(df_data)
    
except KeyboardInterrupt:
    print(" Принудительное завершение программы.")
    