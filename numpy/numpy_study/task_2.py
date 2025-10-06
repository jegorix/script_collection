import numpy as np
from pprint import pprint

n_students = 100
ages = np.random.randint(17, 25, size=n_students)
scores_math, scores_physics, scores_cs = (np.random.randint(0, 100, size=n_students) for i in range(3))
gender = np.random.choice([0,1], size=n_students)

students = np.stack([ages, gender, scores_math, scores_physics, scores_cs]).T


# Indexes and Slices

avg_sum = students[:, 2:5].mean(axis=1)

response1 = {
    'students_older_20': students[students[:, 0] > 20],
    'students_grade_cs_gt_80': students[students[:, 4] > 80],
    'subset': np.vstack([students[:, 0], students[:, 1], avg_sum]).T
}

pprint(response1, indent=4, sort_dicts=False)


# Analytics

response2 = {
    'avg_score_math': np.mean(scores_math),
    'avg_score_physics': np.mean(scores_physics),
    'avg_score_cs': np.mean(scores_cs),
    'max_min_score_math': (np.max(scores_math), np.min(scores_math)),
    'max_min_score_physics': (np.max(scores_physics), np.min(scores_physics)),
    'max_min_score_cs': (np.max(scores_cs), np.min(scores_cs)),
    'corr_matrix': np.corrcoef([scores_math, scores_physics, scores_cs]),
    'mean_cs_men': np.mean(scores_cs[gender == 0]),
    'mean_cs_women': np.mean(scores_cs[gender == 1]),
    'average_score_gender': 'Men better' if np.mean(scores_cs[gender == 0]) > np.mean(scores_cs[gender == 1]) else 'Women better'
}

pprint(response2, indent=4, sort_dicts=False)
print()

# Linear Algebra
scores = np.vstack([scores_math, scores_physics, scores_cs]).T
scores_cov = np.cov(scores, rowvar=False)
eig_values, eig_vectors = np.linalg.eig(scores_cov)


response3 = {
    'scores': scores,
    'scores_cov': np.cov(scores, rowvar=False),
    'eig_values': eig_values,
    'eig_vecrots': eig_vectors
}

pprint(response3, indent=4, sort_dicts=False)


# Save results
np.save('total_scores_cov.npy', arr=scores_cov)
loaded_total = np.load(file='total_scores_cov.npy')

np.savez(file='stats.npz', scores_math=scores_math, scores_physics=scores_physics, scores_cs=scores_cs)
loaded_stats = np.load('stats.npz')

np.savetxt('eig_values.csv', X=eig_values, delimiter=',', fmt='%d')
loaded_csv = np.loadtxt('eig_values.csv', delimiter=',')

response4 = {
    'total_scores_cov': scores_cov,
    'score_math': loaded_stats['scores_math'],
    'score_physics': loaded_stats['scores_physics'],
    'score_cs': loaded_stats['scores_cs'],
    'eig_values': loaded_csv
}

pprint(response4, indent=4, sort_dicts=False)
