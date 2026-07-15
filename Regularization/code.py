# ==========================================
# Regularization in Machine Learning
# Ridge, Lasso and Elastic Net
# ==========================================

# Import Libraries
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet

# ==========================================
# Create Dataset
# ==========================================

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5]
])

y = np.array([
    2,
    4,
    6,
    8,
    10
])

# ==========================================
# Ridge Regression
# ==========================================

ridge = Ridge(alpha=1.0)

ridge.fit(X, y)

print("=" * 50)
print("RIDGE REGRESSION")
print("=" * 50)

print("Coefficient :", ridge.coef_)
print("Intercept  :", ridge.intercept_)
print("Prediction :", ridge.predict([[6]]))

# ==========================================
# Lasso Regression
# ==========================================

lasso = Lasso(alpha=0.1)

lasso.fit(X, y)

print("\n" + "=" * 50)
print("LASSO REGRESSION")
print("=" * 50)

print("Coefficient :", lasso.coef_)
print("Intercept  :", lasso.intercept_)
print("Prediction :", lasso.predict([[6]]))

# ==========================================
# Elastic Net
# ==========================================

elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)

elastic.fit(X, y)

print("\n" + "=" * 50)
print("ELASTIC NET")
print("=" * 50)

print("Coefficient :", elastic.coef_)
print("Intercept  :", elastic.intercept_)
print("Prediction :", elastic.predict([[6]]))