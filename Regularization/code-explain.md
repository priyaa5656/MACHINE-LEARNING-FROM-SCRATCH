# word by Explanation

>1:- Ridge Regression
=========================================
## Step 1- - Import Libraries 

### import numpy as np- 
Imports NumPy for creating arrays

### from sklearn.linear_model import Ridge
Imports the Ridge Regression model.

### from sklearn.linear_model import Lasso
Imports the Lasso Regression model.

### from sklearn.linear_model import ElasticNet
Imports the Elastic Net model.

---
## Step 2-Create Dataset 
### X = np.array([[1],[2],[3],[4],[5]])
Input feature (Study Hours).


### y = np.array([2,4,6,8,10])
Target values.

---
## Step 3- ridge = Ridge(alpha=1.0)
Creates a Ridge Regression model. `alpha` controls the amount of Regularization.

```
Larger alpha
↓
More Regularization.
```

---
## Step 4- ridge.fit(X,y)
Trains the model.

---
## Step 5- ridge.coef_
Returns the coefficient.

---
## Step 6- ridge.intercept_
Returns the intercept.

---
## Step 7- ridge.predict([[6]])
Predicts the value for Study Hours = 6.


===========================================
============================================


>2:- Lasso Regression

## Step 1 to Step 2 same as above ridge model then 


## Step 3- lasso = Lasso(alpha=0.1)
Creates a Lasso model.

---
## Step 4- lasso.fit(X,y)
Trains the Lasso model.

---
## Step 5- lasso.coef_
Returns the coefficient. Some coefficients may become exactly **0**.

---
## Step 6- lasso.predict([[6]])
Predicts the output.




===========================================
============================================


>3:- Elastic Net

## Step 1 to Step 2 same as above ridge model then 


## Step 3- elastic = ElasticNet( alpha=0.1, l1_ratio=0.5)
Creates an Elastic Net model.
```
alpha
↓
Regularization strength.


l1_ratio
↓
Balance between Ridge and Lasso.


0
↓
Pure Ridge


1
↓
Pure Lasso


0.5
↓
Half Ridge + Half Lasso.
```


---
## Step 4- elastic.fit(X,y)
Trains the model.

---
## Step 5- elastic.predict([[6]])
Predicts the output.


---
## Summary
```
Ridge
↓
Reduces coefficient values.

---
Lasso
↓
Makes some coefficients exactly 0.

---
Elastic Net
↓
Uses both Ridge and Lasso together.
```