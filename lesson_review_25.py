import matplotlib.pyplot as plt
import numpy as np

a = np.array([2, 3, 4])
b = np.array([0.5, 1, -0.25])
#1 3 -1
print(np.dot(a,b))

areas = np.array([35, 55, 75])
prices = np.array([3.4, 5.2, 7.0])

w = 0.09
bias = 0.5  

predictions=w * areas + bias
print(predictions)
print(predictions-prices)
plt.scatter(areas, prices, label="Real prices")
plt.plot(areas, predictions, label="areas, predictions")
plt.xlabel("Area, square metres")
plt.ylabel("Price, million RUB")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#везде завысила 