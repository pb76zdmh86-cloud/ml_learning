import numpy as np

# Строки — квартиры
# Столбцы — площадь (м²), число комнат, расстояние до центра (км)
features = np.array([
    [25, 1, 12],  # квартира 1
    [40, 2,  8],  # квартира 2
    [55, 2,  4],  # квартира 3
    [70, 3,  2]   # квартира 4
])
print(features.shape)  # (4, 3)
print(features.size)
print(features.ndim)
print(features[2, :]) 
print(features[:,1:2].shape)
print(features[:,1].shape)
minf=np.min(features, axis=0)
print(minf)
maxf=np.max(features, axis=0)
print(maxf)
averagef=np.mean(features, axis=0, keepdims=True)
print(averagef)
centered_features = features - averagef
print(centered_features)
averagef1=np.mean(features, axis=1, keepdims=True)
print(averagef1)
centered_features1 = features - averagef1
print(centered_features1)
normalized_features = (features - minf) / (maxf - minf)
print(normalized_features)  
print(np.mean(centered_features, axis=0))
print(np.mean(centered_features1, axis=1))
print(np.min(normalized_features, axis=0))
print(np.max(normalized_features, axis=0))
tested_features = np.zeros_like(features, dtype=float)
for i in range(features.shape[0]):      # перебираем строки
    for j in range(features.shape[1]):  # перебираем столбцы
        tested_features[i, j] = features[i, j] + 1
print(np.allclose(tested_features,features+1))
