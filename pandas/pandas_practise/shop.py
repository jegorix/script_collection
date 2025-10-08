import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

df_shop = pd.read_csv(filepath_or_buffer='content/shop.csv',
                   sep=';')

df_shop['result'] = df_shop['price'] * df_shop['quantity']

response = {
    'Общая выручка': df_shop['result'].sum(),
    'топ-3 покупателей по сумме заказов': df_shop.groupby('customer')['result'].sum().sort_values(ascending=False)[:3].to_dict(),
    'Самая популярная категория': df_shop.groupby('category')['result'].sum().sort_values(ascending=False).idxmax(),
}

# График выручки по городам
df_shop.groupby('city')['result'].sum().plot(kind='bar', legend=True)
plt.show()



print(df_shop.to_markdown())
print()
pprint(response, indent=4, sort_dicts=False)