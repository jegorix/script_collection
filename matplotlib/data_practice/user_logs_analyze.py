import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# data
np.random.seed(42)
n_rows = 5000
user_ids = np.random.randint(1, 201, size=n_rows)
event_types = np.random.choice(['view', 'click', 'purchase'], size=n_rows, p=[0.6, 0.3, 0.1])
categories = np.random.choice(['Food', 'Clothes', 'Electronics'], size=n_rows, p=[0.4, 0.35, 0.25])
dates = pd.date_range(start='2025-09-01', end='2025-09-30', freq='min')
event_times = np.random.choice(dates, size=n_rows)
prices = np.where(event_types=='purchase', np.random.randint(5, 501, size=n_rows), 0)

df_logs = pd.DataFrame({
    'user_id': user_ids, 
    'event_type': event_types,
    'event_time': event_times,
    'item_category': categories,
    'price': prices
})
df_logs.to_csv('content/user_logs.csv')


# add columns hour and day
df_user_logs = pd.read_csv('content/user_logs.csv')
df_user_logs['event_time'] = pd.to_datetime(df_user_logs['event_time'])
df_user_logs['day'] = df_user_logs['event_time'].dt.day
df_user_logs['hour'] = df_user_logs['event_time'].dt.hour
print(df_user_logs.head(4))

# user's analytics
user_active_day = df_user_logs.groupby('day')['user_id'].count()
print("\nАктивности пользователей по дням")
print(user_active_day.head(5))

# top 5 most active user's by events
most_active_users = df_user_logs.groupby('user_id')['event_type'].count().sort_values(ascending=False)
print('\nТоп-5 наиболее активных пользователей')
print(most_active_users.head(5))

# user's without purchase
users_without_purchases = df_user_logs.loc[(df_user_logs['event_type'] != 'purchase'), ['user_id', 'price']]
print(f"\nUser's without purchases: {users_without_purchases.count()}")
print(users_without_purchases.head(5))

# sales
print(f'\nGeneral revenue: {df_user_logs['price'].sum()}')


# PLOTS

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# plot user activity by hour 
#  график активности пользователей по часам
# (среднее число событий в каждый час суток)
user_activity_by_hour = df_user_logs.groupby('hour')['user_id'].count()
ax[0, 0].bar(user_activity_by_hour.index, user_activity_by_hour.values, color='orange')
ax[0, 0].set_xticks(range(0, 24, 1))
ax[0, 0].set_title('Average counts of events per hour')
ax[0, 0].set_xlabel('Hours')
ax[0, 0].set_ylabel('Activity')

# sales dynamic by price
prices_by_day = df_user_logs.groupby('day').sum(numeric_only=True)['price']
ax[0, 1].plot(prices_by_day.index, prices_by_day.values, color='lightblue')
ax[0, 1].set_title('Динамика покупок по дням')
ax[0, 1].set_xlabel('День')
ax[0, 1].set_ylabel('Выручка')

# histogram prices distribution
purchase_prices = df_user_logs.loc[df_user_logs['event_type'] == 'purchase', 'price'].values
ax[1, 0].hist(purchase_prices, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax[1, 0].set_title("Распределение цен покупок")
ax[1, 0].set_xlabel("Цена")
ax[1, 0].set_ylabel("Количество")


# plot activation
plt.tight_layout()
plt.show()