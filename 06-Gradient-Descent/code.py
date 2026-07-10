import numpy as np

# Dataset
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Initialize Parameters
m = 0
b = 0

# Hyperparameters
learning_rate = 0.01
epochs = 1000

# Number of Data Points
n = len(X)

# Gradient Descent
for i in range(epochs):

    # Prediction
    y_pred = m * X + b

    # Error
    error = y - y_pred

    # Gradient Calculation
    dm = (-2 / n) * np.sum(X * error)
    db = (-2 / n) * np.sum(error)

    # Update Parameters
    m = m - learning_rate * dm
    b = b - learning_rate * db

# Final Result
print("Slope (m):", round(m, 4))
print("Intercept (b):", round(b, 4))

print("\nFinal Equation")
print(f"y = {round(m,2)}x + {round(b,2)}")