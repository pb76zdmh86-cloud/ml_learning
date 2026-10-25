import numpy as np

# Строки — квартиры
# Столбцы — площадь (м²), количество комнат, расстояние до центра (км)
features = np.array([
    [30, 1, 10],  # квартира 1
    [45, 2,  6],  # квартира 2
    [60, 2,  4],  # квартира 3
    [80, 3,  2],  # квартира 4
    [50, 1,  8]   # квартира 5
])

# Известные цены квартир в миллионах рублей — целевая переменная
prices = np.array([3.0, 4.5, 6.0, 8.5, 4.0])
column_min = np.min(features, axis=0)
print(column_min)
column_max = np.max(features, axis=0)
print(column_max)
normalized_features = (features - column_min) / (column_max - column_min)
print(np.max(normalized_features, axis=0))
print(np.min(normalized_features, axis=0))
print(normalized_features.shape)
print(features)
print(prices.shape)  # (5,)
print(features.shape)  # (5, 3)
result = np.zeros_like(features, dtype=float)
normalized_loop = np.zeros_like(features, dtype=float)
for i in range(features.shape[0]):      # перебираем строки
    for j in range(features.shape[1]):  # перебираем столбцы
        normalized_loop[i, j] = (features[i, j] - column_min[j])/ (column_max[j] - column_min[j])
print(np.allclose(normalized_loop, normalized_features))  # True
#разные потому что prices одномерный массив, а features двумерный массив