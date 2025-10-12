import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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

# Analytics
df_goods['revenue'] = df_goods['quantity'] * df_goods['price']


# FOR CITY
# Revenue for each city
city_revenue = df_goods.groupby('city').sum(numeric_only=True)['revenue']
print("Revenue for each city")
print(city_revenue, end='\n')

# Average product price for each city
city_avg_product_price = df_goods.groupby('city').mean(numeric_only=True)['price']
print("Average product price for each city")
print(city_avg_product_price, end='\n')

# Count of orders for each city
city_product_count = df_goods.groupby('city').count()['quantity']
print("Count of products for each city")
print(city_product_count, end='\n')

# FOR CATEGORIES
category_revenue = df_goods.groupby('category').sum(numeric_only=True)['revenue']
print('Categories revenue')
print(category_revenue)

category_average_units = df_goods.groupby('category')['quantity'].mean()
print('Average quantity of saled good')
print(category_average_units)

# plots

# stacked bar chart: выручка по категориям в каждом городе
pivot_city_categories = df_goods.pivot_table(
    values='revenue',
    index='city',
    columns='category',
    aggfunc='sum',
    fill_value=0
)
print("Выручка по городам и категориям:")
print(pivot_city_categories)

ax = pivot_city_categories.plot(
    kind='bar',
    stacked=True,
    figsize=(10, 6),
    colormap="tab20"
)

ax.set_title('Выручка по категориям в разных городах')
ax.set_ylabel("Выручка")
ax.set_xlabel("Город")
ax.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=50)
plt.tight_layout()
plt.show()

# Line Plot: динамика выручки по категориям
pivot_date_category = df_goods.pivot_table(
    values='revenue',
    index=df_goods['date'].dt.to_period('M'), # группируем по месяцам
    columns='category',
    aggfunc='sum',
    fill_value=0
)

print("\nДинамика выручки по категориям (по месяцам):")
print(pivot_date_category)

ax2 = pivot_date_category.plot(
    kind='line',
    marker='o',
    figsize=(10, 6)
)

ax2.set_title("Динамика выручки по категориям (по месяцам)")
ax2.set_ylabel('Выручка')
ax2.set_xlabel('Месяц')
ax2.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()