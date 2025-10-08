import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

df_orders = pd.read_csv('content/orders.csv', sep=';')

df_orders['total_price'] = df_orders['quantity'] * df_orders['price']

response = {
    'Завершенные заказы': df_orders[df_orders['status'] == 'Completed'],
    'Общая выручка по каждому городу': df_orders.groupby('city')['total_price'].sum().to_dict(),
    'Tоп-3 продукта по выручке': df_orders.groupby('product')['total_price'].sum().sort_values(ascending=False)[:3].to_dict(),
    'Средняя сумма заказа по категориям': df_orders.groupby('category')['total_price'].mean().to_dict(),
    
}

pprint(df_orders)
print()
pprint(response, indent=4, sort_dicts=False)

# График выручки по категориям
df_orders.groupby('category')['total_price'].sum().sort_values(ascending=False).plot(kind='area', legend=True)
plt.title('График выручки по категориям')
plt.xlabel('category')
plt.ylabel('total_price')
plt.show()
