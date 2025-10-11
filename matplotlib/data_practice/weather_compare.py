import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('2023-10-01', periods=30)

minsk_df = pd.DataFrame(data={
    'date': dates,
    'city': 'Minsk',
    'temp_max': np.random.randint(15, 26, size=30),
    'temp_min': np.random.randint(5, 16, size=30),
    'precipitation': np.random.randint(0, 21, size=30),
})

grodno_df = pd.DataFrame(data={
    'date': dates,
    'city': 'Grodno',
    'temp_max': np.random.randint(18, 29, size=30),
    'temp_min': np.random.randint(7, 18, size=30),
    'precipitation': np.random.randint(0, 21, size=30),
})

df_weather = pd.concat([grodno_df, minsk_df], ignore_index=True)
df_weather['average_temp'] = (df_weather['temp_max'] + df_weather['temp_min']) / 2
print(df_weather)

max_precip = df_weather.loc[df_weather.groupby('city')['precipitation'].idxmax()]
print("Дни с максимальными осадками по городам:\n")
print(max_precip[['date', 'precipitation', 'city']])

# show plot
fig, ax1 = plt.subplots(figsize=(10, 6))

# separate cities
minsk = df_weather[df_weather['city'] == 'Minsk']
grodno = df_weather[df_weather['city'] == 'Grodno']

# line of average temperatures
ax1.plot(minsk['date'], minsk['average_temp'], color='red', marker='o', label="Minsk(°C)")
ax1.plot(grodno['date'], grodno['average_temp'], color='blue', marker='s', label="Grodno(°C)")
ax1.set_xlabel('Дата')
ax1.set_ylabel('Средняя температура(°C)')
ax1.tick_params(axis='y', labelcolor='red')


# line of precipitation
ax2 = ax1.twinx()
ax2.bar(minsk['date'], minsk['precipitation'], color='red', alpha=0.3, label='Minsk (мм)')
ax2.bar(minsk['date'], minsk['precipitation'], color='blue', alpha=0.3, label='Grodno (мм)')
ax2.set_ylabel("Осадки (мм)", color="blue")
ax2.tick_params(axis='y', labelcolor='green')

# plot title and legend
plt.title("Сравнение погоды: Минск vs Гродно (октябрь 2023)")
fig.tight_layout()
fig.legend(loc="upper right", bbox_to_anchor=(0.9, 0.9))
plt.show()
