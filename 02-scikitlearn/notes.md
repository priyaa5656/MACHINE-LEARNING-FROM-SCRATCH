# Introduction to Scikit-learn
Scikit-learn is one of the most popular Python libraries for Machine Learning.It provides ready-made Machine Learning algorithms that help us build ML models easily without writing complex mathematical formulas from scratch.

## In Simple word
Scikit-learn is a Python library used to build, train, and test Machine Learning models.

## Why Do We Use Scikit-learn?
Imagine you want to build a House Price Prediction model.

### Without Scikit-learn:
You have to write all mathematical formulas yourself.
You have to implement Linear Regression manually.
You have to calculate errors manually.
You have to optimize the model yourself.
This can take hundreds of lines of code.

### With Scikit-learn:
Just a few lines of code.Scikit-learn does all the difficult work internally.
```python
model = LinearRegression()
model.fit(X, y)
model.predict([[1800]])
```

## What Can Scikit-learn Do?
Scikit-learn provides many Machine Learning algorithms.
Examples:
Linear Regression
Logistic Regression
Decision Tree
Random Forest
KNN
SVM
Naive Bayes
K-Means Clustering

## Real-Life Analogy
Imagine building a house.
Without tools:You cut wood using your hands.It is slow and difficult.
With tools:You use a drill, hammer, and saw.The work becomes much easier.

Scikit-learn is like a toolbox for Machine Learning. Instead of creating every algorithm yourself, you simply use the tools provided by Scikit-learn.

## Installing Scikit-learn
Open the terminal and run:
pip install scikit-learn
OR
If you are using Jupyter Notebook:
!pip install scikit-learn

### Checking Installation
```python
import sklearn
print(sklearn.__version__)
```
Example Output:
1.8.0

This means Scikit-learn is installed successfully.



## First Scikit-learn Program (Easy Explanation)
Imagine you are a house dealer.You know the prices of only three houses.

| House Area | Price    |
| ---------- | -------- |
| 1000 sqft  | ₹20 Lakh |
| 1500 sqft  | ₹30 Lakh |
| 2000 sqft  | ₹40 Lakh |

Now someone asks: 
> "A 1800 sqft house costs how much?"
You don't know the exact answer. So you ask a Machine Learning model to estimate the price. That is exactly what this program does.

---

### Step 1 : Import the Required Libraries
```python
from sklearn.linear_model import LinearRegression
```

### What does this mean?
`sklearn` is a Machine Learning library. Inside this library, there are many algorithms.One of them is **Linear Regression**.We are importing that algorithm.Think like this:

Scikit-learn
│
├── Regression
│      └── Linear Regression
│
├── Classification
│      ├── Logistic Regression
│      ├── Decision Tree
│      ├── Random Forest
│      └── SVM
│
├── Clustering
│      └── K-Means
│
└── Preprocessing

We only need **Linear Regression**, so we import it.
---


```python
pip install scikit-learn numpy
import numpy as np
```

NumPy is another Python library.It helps us store numbers in arrays.Instead of writing
```python
1000
1500
2000
```
NumPy stores them neatly inside an array.
 

---
### Step 2 : Create Input Data
```python
X = np.array([[1000],[1500],[2000])
```

This is called **Feature (Input).** Think of it like giving information to the machine. Here the information is:House Area
House 1 → 1000 sqft
House 2 → 1500 sqft
House 3 → 2000 sqft
The machine only knows the sizes of the houses.


---
# Step 3 : Create Output Data
```python
y = np.array([20,30,40])
```

This is called the **Label (Answer).** These are the correct prices.
1000 sqft → ₹20 Lakh
1500 sqft → ₹30 Lakh
2000 sqft → ₹40 Lak

Now the machine has both:
* House Size
* House Price
So it can start learning.


---
# Step 4 : Create the Machine Learning Model
```python
model = LinearRegression()
```

Imagine hiring a new employee.
Employee = Machine Learning Model

At this moment, the employee has **joined the company** but **has not learned anything yet**.The same thing happens here. The model exists,but it knows nothing.


---
# Step 5 : Train the Model
```python
model.fit(X, y)
```

This is the most important line. `fit()` means:
> "Learn from the data."

The model looks at:
1000 → 20
1500 → 30
2000 → 40
Then it understands: As Area increases, Price also increases.Now the model has learned the pattern. 
Before `fit()`: Model ❌ Doesn't know anything
After `fit()`: Model ✅ Learned the relationship

fit() never predicts.
fit() only learns.

---
# Step 6 : Predict
```python
prediction = model.predict([[1800]])
```
Now we ask the model a question. 
House Area = 1800 sqft
↓
Model
↓
Predict Price

The model thinks:1800 lies between 1500 and 2000. So the price should also lie between 30 and 40.
1000 → 20
1500 → 30
2000 → 40
`It predicts: ₹36 Lakh


---
### Step 7 : Print the Answer
```python
print("Predicted Price:", prediction[0], "Lakhs")
```
Output: Predicted Price: 36.0 Lakhs



---

Code Explanation
1. from sklearn.linear_model import LinearRegression
Means:- Imports the **Linear Regression** algorithm from the Scikit-learn library.

2. import numpy as np
Imports the **NumPy** library, which is used to work with arrays and numerical data.

3. X = np.array([...])
Creates the **input data (Features)**. Here, `X` contains the house areas:
* 1000 sqft
* 1500 sqft
* 2000 sqft

4. y = np.array([...])
Creates the **output data (Labels)**. Here, `y` contains the corresponding house prices:
* ₹20 Lakh
* ₹30 Lakh
* ₹40 Lakh

5. model = LinearRegression()
Creates a new **Linear Regression model**. At this point, the model has not learned anything.

6. model.fit(X, y)
Trains the model using the input data (`X`) and the correct output (`y`).he model learns the relationship between house area and house price.

7. prediction = model.predict([[ 1800 ]])
Asks the trained model to predict the price of a **1800 sqft** house.

8. print(...)
Displays the predicted house price on the screen.


---
### Complete Flow
```text
House Data
↓
Machine Learning Model Created
↓
Model Learns (fit)
↓
New House Comes
↓
Model Predicts Price
↓
Print Result
```
Summary
* `X` → Input (Feature)
* `y` → Output (Label)
* `LinearRegression()` → Creates the model
* `fit()` → Trains the model
* `predict()` → Predicts the output for new data
* `print()` → Displays the result

## 
Training Phase

X --------\
           \
            ---> fit() ---> Model Learns
           /
y --------/

Prediction
1800 sqft
↓
Trained Model
↓
36 Lakhs

---
## Easy Trick to Remember
```text
Data
   ↓
Model
   ↓
fit()
   ↓
Model Learns
   ↓
predict()
   ↓
Answer
```

Remember this flow because you will use it in almost every Machine Learning algorithm.




## Interview Questions

1. What is Scikit-learn?

2. Why do we use Scikit-learn?

3. Difference between fit() and predict()?

4. What is Feature?

5. What is Label?

6. What is NumPy?

7. Why do we use np.array()?