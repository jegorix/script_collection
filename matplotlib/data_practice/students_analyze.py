import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df_students = pd.read_csv('content/students.csv')
print(df_students.head(5))

# General Analytics
print(f"\nКоличество студентов: {df_students['student_id'].count()}")
print(f"\nСредний возраст студентов: {df_students['age'].mean():.1f}")
print(f"\nСредний возраст студентов: {df_students['score'].mean():.2f}")
student_comlete_stat = df_students[df_students['completed'] == 1].count() / df_students['student_id'].count() * 100
print(f"\nПроцент студентов завершивших курсы: {student_comlete_stat['student_id']}%")

# Deep analytics

# Analytics by course
course_average_grade = df_students.groupby('course')['score'].mean()
print(f"\nСредний балл по каждому курсу: {course_average_grade}")

# Average time spend
students_average_time = df_students['hours_spent'].mean()
print(f"\nСреднее время, проведённое студентами: {students_average_time:.2f} hours")

# % completeness by course
course_stats = df_students.groupby('course').agg(
    avg_score=('score', 'mean'),
    avg_hours=('hours_spent', 'mean'),
    precent_completed=('completed', lambda x: x.mean() * 100)
).sort_values('avg_score', ascending=False)

print(course_stats, "\n")

# numpy score analyze
score = df_students['score']
print(f"Средняя оценка: {score.mean():.2f}")
print(f"Медиана: {score.median()}")
print(f"Стандартное отклонение: {score.std():.2f}")
print(f"Прецентили: {np.percentile(score, [25, 50, 75])}")

# Visualisation
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

# hist score distribution
ax[0, 0].hist(score, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
ax[0, 0].set_title("Гистограмма распределение оценок")
ax[0, 0].set_xlabel('Баллы')
ax[0, 0].set_ylabel('Количество студентов')

# Boxplot scores by courses
df_students.boxplot(column='score', by='course', ax=ax[1, 0],
                    patch_artist=True,
                    boxprops=dict(facecolor='lightyellow', color='orange'),
                    medianprops=dict(color="blue", linewidth=2),
                    whiskerprops=dict(color='red', linewidth=1.5),
                    capprops=dict(color='green', linewidth=1.5),
                    showfliers=True
                    )
ax[1, 0].set_title('Boxplot score by courses')
ax[1, 0].set_ylabel('Цена')
ax[1, 0].grid(True, linestyle='--', alpha=0.6)

# Линейный график: часы обучения → оценка
ax[0, 1].scatter(df_students['hours_spent'], df_students['score'], alpha=0.6)
ax[0, 1].set_title("Зависимость: часы обучения → итоговая оценка")
ax[0, 1].set_xlabel('Часы обучения')
ax[0, 1].set_ylabel('Оценка')
ax[0, 1].grid(True, linestyle='--', alpha=0.5)

# HeatMap корелляции
corr = df_students[['score', 'hours_spent', 'age']].corr()
sns.heatmap(corr, annot=True, cmap='YlOrRd', ax=ax[1, 1])
ax[1, 1].set_title("Тепловая карта корреляции признаков")

# plot output
plt.tight_layout()
plt.show()


# Total stats
print(f"\nСамый сложный курс: {course_stats['precent_completed'].idxmin()}")
print(f"\nКурс с лучшими результатами: {course_stats['avg_score'].idxmax()}")

correlation_hours_score = df_students['hours_spent'].corr(df_students['score'])
print(f"Корреляция между временем обучения и результатом: {correlation_hours_score:.2f}")