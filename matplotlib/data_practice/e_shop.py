import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# initial data
dates =  pd.date_range(start='2023-04-01', end='2023-09-30')
categories = np.array(['electronics', 'clothes', 'books', 'toys', 'home'])
cities = np.array(['Minsk', 'Moscow', 'Berlin', 'Warsaw', 'Praga'])
orders_count = len(dates) * 20

# Choose cities, categories and dates
category = np.random.choice(categories, size=orders_count)
city = np.random.choice(cities, size=orders_count)
dates = np.random.choice(dates, size=orders_count)

# prices depends on category
price = []
for c in category:
    if c == 'electronics':
        price.append(np.random.randint(200, 2001))
    elif c == 'clothes':
        price.append(np.random.randint(20, 201))
    elif c == 'books':
        price.append(np.random.randint(5, 51))
    elif c == 'toys':
        price.append(np.random.randint(10, 151))
    else:
        price.append(np.random.randint(50, 501))
        
price = np.array(price)
        
quantity = np.random.randint(1, 6, size=orders_count)


df_goods = pd.DataFrame(data={
    'date': dates,
    'category': category,
    'price': price,
    'quantity': quantity,
    'city': city
})

# df_goods.to_csv('content/e_shop.csv')

# Aналитика
df_goods['revenue'] = df_goods['quantity'] * df_goods['price']

# Динамика выручки по месяцам
monthly_revenue = df_goods.groupby(df_goods['date'].dt.to_period('M')).sum(numeric_only=True)['revenue']

# Динамика выручки по категории
# category_revenue = df_goods.groupby('category')['revenue'].sum()
category_revenue = df_goods.groupby("category").sum(numeric_only=True)['revenue']

# Динамика выручки по категории
city_revenue = df_goods.groupby('city').sum(numeric_only=True)['revenue']


# plots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# revenue dynamics
axes[0, 0].plot(monthly_revenue.index.astype(str), monthly_revenue.values, marker='o', color='green')
axes[0, 0].set_title('Динамика выручки по месяцам')
axes[0, 0].set_xlabel('Месяц')
axes[0, 0].set_ylabel('Выручка')
axes[0, 0].grid(True, linestyle='--', alpha=0.6)

# Pie chart by categories
axes[0, 1].pie(category_revenue.values, labels=category_revenue.index.astype(str),
               autopct="%1.1f%%", startangle=90, explode=(0.3, 0, 0, 0, 0))

axes[0, 1].set_title('Распределение выручки по категориям', loc='left', pad=50)


# (1,0) Bar chart by cities
axes[1, 0].bar(city_revenue.index, city_revenue.values, color='skyblue', edgecolor="black")
axes[1, 0].set_title("Выручка по городам")
axes[1, 0].set_xlabel("Город")
axes[1, 0].set_ylabel("Выручка")
axes[1, 0].grid(True, linestyle='--', alpha=0.6)


# (1,1) Boxplot price
df_goods.boxplot(column='price', by='category', ax=axes[1,1], patch_artist=True,
                 boxprops=dict(facecolor='lightyellow', color='orange'),
                 medianprops=dict(color='red', linewidth=2))

axes[1,1].set_title("Распределение цен по категориям")
axes[1,1].set_ylabel("Цена")
axes[1,1].grid(True, linestyle='--', alpha=0.6)


fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
