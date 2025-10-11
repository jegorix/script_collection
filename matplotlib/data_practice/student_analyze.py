import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


df_students = pd.DataFrame(data={
    'students':  np.array([f'Student_{i}' for i in range(1, 51)]),
    'math_score': np.random.randint(40, 101, size=50),
    'cs_score': np.random.randint(30, 101, size=50),
    'eng_score': np.random.randint(20, 101, size=50) 
})

# total score
df_students['total_score'] = df_students['math_score'] + df_students['cs_score'] + df_students['eng_score']
df_students.sort_values('total_score', ascending=False)
print(df_students.sort_values('total_score', ascending=False))

print("Топ-5 студентов по суммарному баллу:")
print(df_students.sort_values('total_score', ascending=False).head(3))


# top 3 students with highest grade in math
best_students = df_students[df_students['math_score'] == df_students['math_score'].max()]
print('Best student in math')
print(best_students[['students', 'math_score']])

# plot
fig, ax1 = plt.subplots(nrows=1, ncols=2, figsize=(10, 6))

# hist scores in math
ax1[0].hist(df_students['math_score'], density=True, bins=10, facecolor='g', alpha=0.75, label='math hist')
ax1[0].grid(True, color='blue', linestyle='--', alpha=0.6)
ax1[0].set_xlabel('math scores')
ax1[0].set_ylabel('Density')
ax1[0].tick_params(axis='y', labelcolor='blue')

# boxplot all scores in subjects
ax1[1].boxplot([df_students['math_score'], df_students['cs_score'], df_students['eng_score']],
               labels=['Math', 'CS', 'English'],
               patch_artist=True, boxprops=dict(facecolor="lightblue"),
               medianprops=dict(color='red', linewidth=2)
               )

ax1[1].set_ylabel('Scores')
# plt.xticks([1, 2, 3], ['math_score', 'cs_score', 'eng_score'])
ax1[1].tick_params(axis='y', labelcolor='red')
ax1[1].grid(True, color='blue', linestyle='--', alpha=0.6)

# plot title and legend
fig.suptitle("Student Scores Analytics", fontsize=14, fontweight="bold")
# plt.title('Student scores analytics')
fig.tight_layout()
fig.legend(loc='upper center', bbox_to_anchor=(0.2, 1))
plt.show()

plt.show()

