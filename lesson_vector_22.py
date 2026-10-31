import numpy as np

# Площадь, количество комнат, расстояние до центра
features = np.array([50, 2, 8])

# Учебные коэффициенты модели для этих трёх признаков
weights = np.array([0.08, 0.4, -0.05])
print(features.shape)
print(weights.shape)
#4.4
print(features * weights)#массив умножили на массив
resultat=features * weights
suma=np.sum(resultat)
print(suma)
print(np.dot(features, weights))