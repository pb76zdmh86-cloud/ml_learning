import numpy as np
import matplotlib.pyplot as plt

# Известные площади и цены пяти квартир
areas = np.array([30, 45, 60, 80, 50])
prices = np.array([3.0, 4.5, 6.0, 8.5, 4.0])

# Площади для начала и конца каждой прямой
x_line = np.array([20, 90])
plt.scatter(areas, prices, label="Real prices")

y_a = 0.10 * x_line + 0
plt.plot(x_line, y_a, label="A: w=0.10, b=0")

y_b= 0.08 * x_line + 1
plt.plot(x_line, y_b, label="B: w=0.08, b=1")

y_c = 0.12 * x_line - 1
plt.plot(x_line, y_c, label="C: w=0.12, b=-1")

plt.xlabel("Area, square metres")
plt.ylabel("Price, million RUB")
plt.title("Apartment prices and linear models")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

