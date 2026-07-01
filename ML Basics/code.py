"""
===========================================
Day 1 - Machine Learning Fundamentals
First Machine Learning Program
===========================================

Topic:
- What is Machine Learning?
- First Scikit-Learn Model
"""

# Import Linear Regression model
from sklearn.linear_model import LinearRegression

# Import NumPy
import numpy as np

# ---------------------------------------
# Step 1 : Create Input Data (Features)
# ---------------------------------------

# House area in square feet
X = np.array([
    [1000],
    [1500],
    [2000]
])

# ---------------------------------------
# Step 2 : Create Output Data (Labels)
# ---------------------------------------

# House price in Lakhs
y = np.array([
    20,
    30,
    40
])

# ---------------------------------------
# Step 3 : Create Machine Learning Model
# ---------------------------------------

model = LinearRegression()

# ---------------------------------------
# Step 4 : Train the Model
# ---------------------------------------

model.fit(X, y)

# ---------------------------------------
# Step 5 : Predict New House Price
# ---------------------------------------

prediction = model.predict([[1800]])

# ---------------------------------------
# Step 6 : Print Result
# ---------------------------------------

print("Predicted Price:", prediction[0], "Lakhs")