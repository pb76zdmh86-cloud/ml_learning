import numpy as np
from matplotlib import pyplot as plt

areas = np.array([30, 45, 60, 80, 50])
prices = np.array([3.0, 4.5, 6.0, 8.5, 4.0])
w = 0.10
b = 0.0
predictions = areas * w + b
def mse(predictions, prices):
    return ((predictions - prices) ** 2).mean()

print(mse(predictions, prices))
print(mse(prices,prices))
print(mse(prices + 2, prices))

models = [
    ("A", 0.10, 0.0),
    ("B", 0.08, 1.0),
    ("C", 0.12, -1.0),
    ("D", 0.09, 0.5),
    ("E", 0.10, -0.25),
    ("F", 0.11, -0.5),
]
for name,w,n in models:
    predictions = areas * w + n
    print(name, mse(predictions, prices))

x_line = np.array([30, 80])
plt.scatter(areas, prices, label="Real prices")

y_a = 0.10 * x_line + 0.0
plt.plot(x_line, y_a, label="A: w=0.10, b=0")

y_f = 0.11 * x_line - 0.5
plt.plot(x_line, y_f, label="F: w=0.11, b=-0.5")

plt.xlabel("Area, square metres")
plt.ylabel("Price, million RUB")
plt.title("Apartment prices and linear models")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()