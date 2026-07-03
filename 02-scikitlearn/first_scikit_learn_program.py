"""
=========================================
First Scikit-learn Program
=========================================

Problem Statement:
We know the prices of only three houses.
Our goal is to predict the price of a new
house with an area of 1800 sqft.
"""

# =========================================
# Step 1 : Import Required Libraries
# =========================================

from sklearn.linear_model import LinearRegression
import numpy as np

print("=" * 50)
print("First Scikit-learn Program")
print("=" * 50)

# =========================================
# Step 2 : Create Input Data (Features)
# =========================================

print("\nStep 2 : Creating Input Data (X)")

X = np.array([
    [1000],
    [1500],
    [2000]
])

print(X)

# =========================================
# Step 3 : Create Output Data (Labels)
# =========================================

print("\nStep 3 : Creating Output Data (y)")

y = np.array([
    20,
    30,
    40
])

print(y)

# =========================================
# Step 4 : Create Model
# =========================================

print("\nStep 4 : Creating Linear Regression Model")

model = LinearRegression()

print("Model Created Successfully")

# =========================================
# Step 5 : Train Model
# =========================================

print("\nStep 5 : Training Model")

model.fit(X, y)

print("Model Training Completed")

# =========================================
# Step 6 : Prediction
# =========================================

print("\nStep 6 : Predicting House Price")

new_house = [[1800]]

prediction = model.predict(new_house)

# =========================================
# Step 7 : Result
# =========================================

print("\n========== RESULT ==========")

print("House Area :", new_house[0][0], "sqft")

print("Predicted Price :", prediction[0], "Lakhs")

print("============================")