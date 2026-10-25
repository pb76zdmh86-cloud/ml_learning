import numpy as np

a = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a)
print("Размеры:", a.shape)
print("Количество элементов:", a.size)
print("Количество измерений:", a.ndim)
print("Тип данных:", a.dtype)
print(a[1:,1])