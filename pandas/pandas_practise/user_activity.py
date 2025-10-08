import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint

df_activity = pd.read_csv('content/user_activity.csv', sep=';')

df_activity['date'] = pd.to_datetime(df_activity['date'])


response = {
    'Общее время проведенное на сайте': int(df_activity['time_spent'].sum()),
    'топ-3 страниц по суммарному времени': df_activity.groupby('page')['time_spent'].sum().sort_values(ascending=False)[:3].to_dict(),
    'Какие устройства чаще всего используют пользователи': df_activity.value_counts('device').sort_values(ascending=False).to_dict(),
}

pprint(df_activity.to_markdown())
print()
pprint(response, indent=4, sort_dicts=False)

# График суммарного времени на сайте по дням
df_activity.groupby('date')['time_spent'].sum().sort_index().plot(kind='bar', legend=True)
plt.title('Суммарное время на сайте по дням')
plt.xlabel('Дата')
plt.ylabel('Время (мин)')
plt.show()