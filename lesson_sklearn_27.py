import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def mse(predictions, prices):
    return ((predictions - prices) ** 2).mean()
def mae(predictions, prices):
    return np.abs(predictions - prices).mean()

areas = np.array([28, 32, 37, 42, 46, 51, 55, 60, 64, 69, 75, 82])
prices = np.array([3.1, 3.5, 3.6, 4.4, 4.5, 5.3, 5.0, 6.1, 6.4, 6.6, 7.5, 8.0])


X = areas.reshape(-1, 1)
y = prices

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

print(y_test)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

mean_y_train = np.mean(y_train)
mean_price = y_train.mean()
baseline_predictions = np.full(len(X_test), mean_price)
print(baseline_predictions)
print(mse(baseline_predictions, y_test))
print(mae(baseline_predictions, y_test))
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)
print(mse(predictions, y_test))
print(mae(predictions, y_test))
print("w:", model.coef_[0])
print("b:", model.intercept_)