import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# === Данные для обработки ===
np.random.seed(42)
n_rows = 5000
user_ids = np.random.randint(1, 201, size=n_rows)
event_types = np.random.choice(['view', 'click', 'purchase'], size=n_rows, p=[0.6, 0.3, 0.1])
categories = np.random.choice(['Food', 'Clothes', 'Electronics'], size=n_rows, p=[0.4, 0.35, 0.25])
dates = pd.date_range(start="2025-09-01", end="2025-09-30", freq="min")
event_times = np.random.choice(dates, size=n_rows)
prices = np.where(event_types == 'purchase', np.random.randint(5, 501, size=n_rows), 0)

df_logs = pd.DataFrame({
    'user_id': user_ids,
    'event_type': event_types,
    'event_time': event_times,
    'item_category': categories,
    'price': prices
})

df_logs.to_csv("user_logs.csv", index=False)
print("CSV файл 'user_logs.csv' успешно создан!")



# === Подготовка данных ===
df_orders = pd.read_csv('content/orders.csv')
df_orders['total_price'] = df_orders['quantity'] * df_orders['price']
df_orders['date'] = pd.to_datetime(df_orders['date'])
df_orders['day_of_week'] = df_orders['date'].dt.day_name()


# === Статистика ===
purchase_prices = df_logs.loc[df_logs['event_type'] == 'purchase', 'price'].values

print("\nTotal revenue:", df_orders['total_price'].sum())
print("\nUnique customers:", df_orders['customer_id'].nunique())
print("\nAverage order price:", df_orders['total_price'].mean())
print("\nMedian order price:", df_orders['total_price'].median())
print("\nStandard deviation:", f"{df_orders['total_price'].std():.6}")
print(f"Перцентили (25%, 50%, 75%): {np.percentile(purchase_prices, [25, 50, 75])}")



# === Аналитика по категориям ===
category_revenue = df_orders.groupby('category')['total_price'].sum()
category_average_order = df_orders.groupby('category')['total_price'].mean()



# === Аналитика по времени ===
monthly_revenue = df_orders.groupby(df_orders['date'].dt.to_period('M'))['total_price'].sum()
print("\nМесяц с наибольшими продажами:\n", monthly_revenue.loc[monthly_revenue.idxmax()])



# === Топ продукты и клиенты ===
products_revenue = df_orders.groupby('product')['total_price'].sum().sort_values(ascending=False).head(5)
customers_revenue = df_orders.groupby('customer_id')['total_price'].sum().sort_values(ascending=False).head(5)



# === Построение графиков ===
fig, ax = plt.subplots(3, 3, figsize=(14, 10))



# Bar chart: категории
ax[0, 0].bar(category_revenue.index, category_revenue.values, color='skyblue')
ax[0, 0].set_title('Выручка по категориям')
ax[0, 0].set_xlabel('Категория')
ax[0, 0].set_ylabel('Выручка')
ax[0, 0].grid(True, linestyle='--', alpha=0.6)



# Line: динамика выручки
ax[1, 0].plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', color='green')
ax[1, 0].set_title('Динамика выручки по месяцам')
ax[1, 0].set_xlabel('Месяц')
ax[1, 0].set_ylabel('Выручка')
ax[1, 0].grid(True, linestyle='--', alpha=0.6)



# Barh: топ-5 товаров
ax[0, 1].barh(products_revenue.index, products_revenue.values, color='orange')
ax[0, 1].set_title('Топ-5 товаров по выручке')
ax[0, 1].set_xlabel('Выручка')
ax[0, 1].grid(True, linestyle='--', alpha=0.6)



# Barh: топ-5 клиентов
ax[1, 1].barh(customers_revenue.index.astype(str), customers_revenue.values, color='purple')
ax[1, 1].set_title('Топ-5 клиентов по сумме покупок')
ax[1, 1].set_xlabel('Сумма покупок')
ax[1, 1].grid(True, linestyle='--', alpha=0.6)



# Boxplot: цены заказов по категориям
df_orders.boxplot(column='total_price', by='category', ax=ax[2, 0],
                  patch_artist=True,
                  boxprops=dict(facecolor='lightyellow', color='orange'),
                  medianprops=dict(color='red', linewidth=2),
                  whiskerprops=dict(color="blue", linewidth=1.5),
                  capprops=dict(color="blue", linewidth=1.5),
                  showfliers=True)  # показываем выбросы
ax[2, 0].set_title('Boxplot итоговой цены по категориям')
ax[2, 0].set_ylabel('Цена')
ax[2, 0].grid(True, linestyle='--', alpha=0.6)



# Pie chart: категории
ax[2, 1].pie(category_revenue.values,
             labels=category_revenue.index,
             autopct="%1.1f%%",
             startangle=90,
             explode=[0.05]*len(category_revenue))
ax[2, 1].set_title("Распределение выручки по категориям")




# Heatmap: заказы по дням недели
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
pivot_day_order = df_orders.pivot_table(index='day_of_week', 
                                        values='quantity', 
                                        aggfunc='sum').reindex(days_order)

sns.heatmap(pivot_day_order,
            annot=True,
            fmt='d',
            cmap='YlOrRd',
            ax=ax[0, 2])
ax[0, 2].set_title('Количество заказов по дням недели')


# Histogram: Гистограма распределения цен
ax[1, 2].hist(purchase_prices, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax[1, 2].set_title("Распределение цен покупок")
ax[1, 2].set_xlabel("Цена")
ax[1, 2].set_ylabel("Количество")


# Вывод всех графиков
plt.tight_layout()
plt.show()



# === Корреляция ===
cor_quantity_price = np.corrcoef(df_orders['quantity'], df_orders['price'])
print('\nКорреляция между количеством товара и его ценой:\n', cor_quantity_price)


# ---- NumPy-анализ ----



# === Сохранение новых данных ===
df_orders.to_csv('content/orders_updated.csv')
print("✅ Файл 'orders_updated.csv' успешно сохранён!")