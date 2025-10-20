from datetime import datetime
from models import Category
from storage import load_app_usage_json, TEST_FILE, app_usage_data_to_dataframe
from analytics import Analytics

#     schema = AppUsageSchema(
#     app='Telegram',
#     category=Category("Social"),
#     minutes=20,
#     date=datetime.now(),
#     comment="Some comment"
# )
#     transaction = schema.to_app_usage()
#     save_app_usage_json([transaction])


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