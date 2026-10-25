import numpy as np

# Столбцы — три испытания
scores = np.array([
    [10, 15, 20],  # участник 1
    [12, 18, 16],  # участник 2
    [14, 10, 18],  # участник 3
    [20, 16, 12]   # участник 4
])
bonus_scores = scores + 2
scaled_scores = scores * 1.5
percent_scores = scores / 20 * 100
print(np.mean(percent_scores,axis=1))  
print("дополнительные баллы:\n", bonus_scores)
print("масштабированные баллы:\n", scaled_scores)
print("процентные баллы:\n", percent_scores)
