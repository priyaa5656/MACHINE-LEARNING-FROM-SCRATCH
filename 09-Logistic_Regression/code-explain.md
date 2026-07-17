# Line-by-Line Explanation

---
## Step 1-  import numpy as np
Import NumPy . Used to create arrays.

---
## Step 2- from sklearn.linear_model import LogisticRegression
Imports Logistic Regression model from Scikit-learn.

---
## Step 3- X = np.array(...) 
Input Data- Stores Study Hours.



## Step 4-y = np.array(...)
Target Data- Stores Pass / Fail.

0 = Fail      
1 = Pass


---
## Step 5 - model = LogisticRegression()
Create Model - Creates a Logistic Regression model.

---
## Step 6- model.fit(X, y)
Train Model - Learns from the training data.

---
## Step 7- model.predict([[6]])
Predict Class - Predicts whether a student who studied 6 hours will Pass or Fail.
Output
```text
1
↓
Pass
```

---
## Step 8- model.predict_proba([[6]])
Predict Probability - Returns probabilities.
Example: 
```text
[[0.15 0.85]]
```

Meaning: 
```text
15% Fail

85% Pass
```

---
## Workflow
```text
Dataset
↓
LogisticRegression()
↓
fit()
↓
predict()
↓
predict_proba()
```