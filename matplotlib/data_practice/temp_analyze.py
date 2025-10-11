import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

temp_min = np.random.randint(5, 16, size=30)
temp_max = np.random.randint(15, 26, size=30)
precipitation = np.random.randint(0, 21, size=30)

dates = pd.date_range('2023-10-01', periods=30)

df_weather = pd.DataFrame(data={
    'date': dates,
    'temp_min': temp_min,
    'temp_max': temp_max,
    'precipitation': precipitation
})

df_weather['temp_average'] = (temp_min + temp_max) / 2

# day with max precepitation
max_precip_day = df_weather.loc[df_weather['precipitation'].idxmax()]
print("День с максимальной осадкой:")
print(max_precip_day[["date", "precipitation"]])

fig, ax1 = plt.subplots(figsize=(10,5))

# Line of average temperature
ax1.plot(df_weather['date'], df_weather['temp_average'], color='red', marker='o', label="Средняя температура (°C)")
ax1.set_xlabel("Дата")
ax1.set_ylabel("Температура")

# Second axis Y for preciptation
ax2 = ax1.twinx()
ax2.plot(df_weather['date'], df_weather['precipitation'], alpha=0.3, color='blue', label="Осадки (мм)")
ax2.set_ylabel("Осадки (мм)", color="blue")
ax2.tick_params(axis='y', labelcolor='blue')

# header of legend
plt.title("Температура и осадки за октябрь 2023")
fig.tight_layout()
plt.show()