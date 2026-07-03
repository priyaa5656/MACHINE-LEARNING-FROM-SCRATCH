"""
=========================================================
Linear Regression
Machine Learning From Scratch
=========================================================

Topics Covered
--------------
1. Import Libraries
2. Create Dataset
3. Create Linear Regression Model
4. Train Model
5. Predict New Values
6. Multiple Predictions
7. Slope (m)
8. Intercept (b)
9. User Input Prediction

=========================================================
"""

# ============================================
# Step 1 : Import Libraries
# ============================================

from sklearn.linear_model import LinearRegression
import numpy as np


# ============================================
# Step 2 : Create Dataset
# ============================================

# X = Input (Feature)
# House Area (Square Feet)

X = np.array([
    [1000],
    [1500],
    [2000]
])

# y = Output (Label)
# House Price (Lakhs)

y = np.array([
    20,
    30,
    40
])


# ============================================
# Display Dataset
# ============================================

print("=" * 50)
print("HOUSE PRICE DATASET")
print("=" * 50)

for area, price in zip(X, y):
    print(f"Area : {area[0]} sqft\tPrice : ₹{price} Lakhs")


# ============================================
# Step 3 : Create Model
# ============================================

print("\nCreating Linear Regression Model...")

model = LinearRegression()


# ============================================
# Step 4 : Train Model
# ============================================

print("Training Model...")

model.fit(X, y)

print("Model Trained Successfully!")


# ============================================
# Step 5 : Predict New House Price
# ============================================

print("\n" + "=" * 50)
print("SINGLE PREDICTION")
print("=" * 50)

prediction = model.predict([[1800]])

print("House Area : 1800 sqft")
print("Predicted Price :", prediction[0], "Lakhs")


# ============================================
# Step 6 : Multiple Predictions
# ============================================

print("\n" + "=" * 50)
print("MULTIPLE PREDICTIONS")
print("=" * 50)

areas = [1200, 1700, 2200, 2500, 3000]

for area in areas:

    price = model.predict([[area]])

    print(f"{area} sqft ---> {price[0]:.2f} Lakhs")


# ============================================
# Step 7 : Model Formula
# ============================================

print("\n" + "=" * 50)
print("MODEL DETAILS")
print("=" * 50)

print("Slope (m)      :", model.coef_[0])

print("Intercept (b)  :", model.intercept_)


print("\nLinear Regression Formula")

print(f"Price = ({model.coef_[0]}) × Area + ({model.intercept_})")


# ============================================
# Step 8 : User Prediction
# ============================================

print("\n" + "=" * 50)
print("TRY YOUR OWN INPUT")
print("=" * 50)

area = float(input("Enter House Area (sqft): "))

predicted_price = model.predict([[area]])

print("\nEstimated House Price")

print("-------------------------")

print("Area :", area, "sqft")

print("Price:", round(predicted_price[0], 2), "Lakhs")


# ============================================
# Step 9 : Summary
# ============================================

print("\n" + "=" * 50)
print("SUMMARY")
print("=" * 50)

print("✔ Input (X)      : House Area")

print("✔ Output (y)     : House Price")

print("✔ Model          : Linear Regression")

print("✔ fit()          : Train the model")

print("✔ predict()      : Predict new values")

print("✔ coef_          : Slope (m)")

print("✔ intercept_     : Intercept (b)")


print("\nLinear Regression Demo Completed Successfully!")