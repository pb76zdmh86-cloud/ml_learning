import numpy as np

# Строки — студенты, столбцы — математика, физика, информатика
grades = np.array([
    [5, 4, 5],
    [3, 4, 4],
    [4, 5, 5],
    [2, 3, 4],
    [5, 5, 4]
])
print(grades.shape)#1
print(grades.size)#1
print(grades.ndim)#1
print(grades[2,0:])#2
print(grades[0:,2])#3
print(grades[:3,:2])#4
print(np.mean(grades))#5
print(np.min(grades))#6
print(np.max(grades))#6
print(np.mean(grades, axis=1))#7
print(np.mean(grades, axis=0))  # 8