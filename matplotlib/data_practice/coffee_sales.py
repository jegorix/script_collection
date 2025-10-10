import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

coffee_data = pd.read_csv('content/coffee_sales.csv',
                          delimiter=',')

# revenue for each row
coffee_data['revenue'] = coffee_data['quantity'] * coffee_data['price']

# revenue for each day
daily_revenue = coffee_data.groupby('date')['revenue'].sum()

# revenue for types of coffee
coffee_revenue = coffee_data.groupby('coffee_type')['revenue'].sum()
most_profitable = coffee_revenue.idxmax()

response = {
    'revenue for each day': daily_revenue,
    'revenue for types of coffee': coffee_revenue,
    'most profitable': most_profitable,
}

pprint(response)

# Plot
plt.figure(figsize=(8,5))
# x - days, y - revenue
daily_revenue.plot(kind='bar', color='skyblue')
plt.title('revenue')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.legend()
plt.show()

