# 💻 Logistic Regression Python Program


# Step 1 : Import Libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sympy import python

# Step 2 : Create Dataset

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

#Study Hours


y = np.array([
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1
])

#Result

# 0 = Fail

# 1 = Pass




# Step 3 : Create Model
model = LogisticRegression()


# Step 4 : Train Model
model.fit(X, y)


#The model learns the relationship between
#Study Hours -> Pass / Fail


# Step 5 : Prediction
prediction = model.predict([[6]])
print(prediction)

# Output :
[1]

## Meaning :Pass


# Step 6 : Probability
probability = model.predict_proba([[6]])
print(probability)

# Output:
0.15, 0.85

#Meaning

#15% - Fail
#85% - Pass


# Complete Program
import numpy as np
from sklearn.linear_model import LogisticRegression

# Dataset

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

y = np.array([
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1
])

# Model
model = LogisticRegression()

# Training
model.fit(X, y)

# Prediction
prediction = model.predict([[6]])
print("Prediction :", prediction)

# Probability
probability = model.predict_proba([[6]])
print("Probability :", probability)
