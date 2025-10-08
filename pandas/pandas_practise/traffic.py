import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt

traffic_data = pd.read_csv('content/traffic.csv',
                           sep=';')

top_values = traffic_data.sort_values('time_spent', ascending=False)[:3]

response = {
    'Общая проведенное время': int(traffic_data['time_spent'].sum()),
    'Топ страницы по времени просмотра': [
        f"{top_value['page']}({top_value['city']}) - {top_value['time_spent']}" for _, top_value in top_values.iterrows()
    ],
    'Популярные устройства': traffic_data.value_counts('device').to_dict(),
    'Среднее время по городам': traffic_data.groupby(['city'])['time_spent'].mean().to_dict()
}

print(traffic_data.to_markdown())
print()
pprint(response, indent=4, sort_dicts=False)

# График посещаемости
traffic_data['date'] = pd.to_datetime(traffic_data['date'])
traffic_data.groupby('date')['user_id'].count().sort_index().plot(kind='line', marker='o')
plt.show()
