import numpy as np

areas = np.array([30, 45, 60, 80, 50])
prices = np.array([3.0, 4.5, 6.0, 8.5, 4.0])

w = 0.12
b = 0.0

predictions=w * areas + b
print(predictions)
print(prices)
difference=predictions-prices
print(difference)#положительная значит что предсказание ошиблось в большую сторону,
#а отрицательное в меньшую
#прибавки получились разные у квартиры с 30 метрами выросло на 0.6 а у квартиры с 80 на 1.6