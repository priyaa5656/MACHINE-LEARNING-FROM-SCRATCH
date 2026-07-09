# What is Train/Test Split?
Before building a Machine Learning model, we need to divide our dataset into two parts.
1. Training Data
2. Testing Data
This process is called **Train/Test Split**.

---

## In Simple Words

Imagine you are preparing for an exam. You first study from books. After studying, you give an exam to check your knowledge.
Machine Learning works in the same way. First, the model learns from the Training Data. Then, it is tested using the Testing Data.
```
Dataset
      │
      ├── Training Data
      │        ↓
      │     Model Learns
      │
      └── Testing Data
               ↓
         Model Gives Test
```


## Why Do We Need Train/Test Split?
Imagine a teacher gives you the same questions in the exam that you already memorized. 
Will that prove you are intelligent?
No.

It only proves that you memorized the answers.The same thing happens in Machine Learning. If we train and test on the same data,the model may simply memorize the answers.It will not learn the real pattern. That is why we divide the data.
Training Data → Learn
Testing Data → Check Performance

## What is Training Data?
Training Data is the data used to teach the Machine Learning model. The model studies this data and learns the relationship between input and output.

Example:
| House Area | Price |
|------------|-------|
|1000        |20|
|1500        |30|
|2000        |40|

The model learns:
1000 → 20
1500 → 30
2000 → 40
This learning process is called **Training**.

Simply remember:
> Training Data = Study Material

## What is Testing Data?

Testing Data is the data that the model has never seen before. It is used to check whether the model has learned correctly.
Example:
Training Data
1000 → 20
1500 → 30

Testing Data
1800 → ?
Now the model predicts the answer.If the prediction is close to the real value, the model is performing well.

Simply remember:
> Testing Data = Final Exam


# Why Do We Divide the Data?
Suppose we have 100 house records. If we use all 100 records for training, then the model already knows every answer. We cannot check whether it can predict new houses. So we divide the data.
Example:
```text
100 Records
↓
80 Records → Training
20 Records → Testing
```
Now the model learns from 80 records. The remaining 20 records are used to test the model. This gives a fair evaluation.

# Common Split Ratios
There is no fixed rule. Some common ratios are:

| Training | Testing |
|----------|----------|
|80%|20%|
|70%|30%|
|90%|10%|

The most commonly used ratio is: 80% Training ,  20% Testing


# What is random_state?

Before splitting, Scikit-learn shuffles the data randomly. 
Every time you run the program, the split may be different. If you use:

```python
random_state=42
```

the split remains the same every time. This helps us reproduce the same results.
Simply remember:
>random_state = Same shuffle every time.

⚙️ Basic Syntax
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42)
```

## First Train/Test Split Program
Now let's divide our dataset into **Training Data** and **Testing Data** using Scikit-learn.

```python
from sklearn.model_selection import train_test_split
import numpy as np

# Input Data (House Area)
X = np.array([ [1000],[1200], [1500], [1800], [2000], [2200], [2500], [2800],[3000],[3500]])

# Output Data (House Price)
y = np.array([ 20, 24, 30,36,40,44,50,56,60,70])

# Split the Data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Print Training Data
print("Training Features:")
print(X_train)

print("\nTraining Labels:")
print(y_train)

# Print Testing Data
print("\nTesting Features:")
print(X_test)

print("\nTesting Labels:")
print(y_test)
```

---

## Example Output

```text
Training Features:
[[2500][1000][2200][1500][3500][2000][1800][3000]]

Training Labels:
[50 20 44 30 70 40 36 60]

Testing Features:
[[1200]
 [2800]]

Testing Labels:
[24 56]
```

## Code Explanation

### Import train_test_split:- from sklearn.model_selection import train_test_split
This imports the **train_test_split()** function from Scikit-learn. We use it to divide the dataset into Training Data and Testing Data.

---
## Import NumPy:- import numpy as np
NumPy helps us create arrays.

---
## Create Input Data: X = np.array([...])
`X` contains the **Features (Input)**. In this example, X stores the **House Areas**.

---
## Create Output Data:- y = np.array([...])
`y` contains the **Labels (Output)**. These are the actual house prices.

---
## Split the Dataset:-  X_train, X_test, y_train, y_test = train_test_split( X,y,test_size=0.2, random_state=42)
This is the most important line. The dataset is divided into four parts.
- `X_train` → Training Features
- `X_test` → Testing Features
- `y_train` → Training Labels
- `y_test` → Testing Labels

---
## test_size = 0.2 :- 
This means: 20% of the data will be used for testing. The remaining 80% will be used for training.

---
## random_state = 42:- 
This keeps the split the same every time you run the program. Without it,the train and test data may change every time.

---
## Print Training Data :- print(X_train)
Displays the training features.

---
## Print Testing Data:- print(X_test)
Displays the testing features.

---
## Print Training Labels:- print(y_train)
Displays the correct answers for the training data.

---
## Print Testing Labels:- print(y_test)
Displays the correct answers for the testing data.

# Summary

- Train/Test Split divides the dataset into two parts.
- Training Data is used to teach the Machine Learning model.
- Testing Data is used to evaluate the model.
- We divide the data to check how well the model performs on unseen data.
- The most common split ratio is **80% Training** and **20% Testing**.
- `train_test_split()` is provided by the Scikit-learn library.
- `test_size` decides how much data will be used for testing.
- `random_state` ensures the same split every time.

---

# Complete Flow

```text
Dataset
   │
   ▼
Train/Test Split
   │
   ├───────────────┐
   ▼               ▼
Training Data   Testing Data
   │               │
   ▼               │
Model Learns       │
   │               │
   └──────┬────────┘
          ▼
     Evaluate Model
          ▼
     Good Prediction
```

---

# Easy Trick to Remember

```text
Study Material
       ↓
Training Data

Final Exam
       ↓
Testing Data
```

OR

```text
Dataset
     ↓
Split
     ↓
Train
     ↓
Test
     ↓
Result
```

---

### Question 1 for solving 
Create a dataset of student marks.

| Study Hours | Marks |
|-------------|-------|
|1|40|
|2|50|
|3|60|
|4|70|
|5|80|
|6|90|
|7|95|
|8|98|

Split the dataset into:
- 80% Training
- 20% Testing

---
### Question 2
Change
```python
test_size = 0.2
to
test_size = 0.3
```
Observe the output. How many rows are now in the Testing Data?

---
### Question 3
Change
```python
random_state = 42
to
random_state = 10
```
Observe the difference.

---
### Question 4
Remove
```python
random_state
```
Remove random_state and run the program three times. Does the output remain the same? Why?



## Homework Solutions

## Solution 1.
### Create a dataset of student marks.

```python
import numpy as np
from sklearn.model_selection import train_test_split

# Input (Study Hours)
X= np.array([ 1,2,3,4,5,6,7,8])


# Output (Marks)
Y = np.array([ [40],[50],[60],[70],[80],[90],[95],[98]])


# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X,Y,  test_size=0.2,   random_state=42)


print("Training Features:")
print(X_train)

print("\nTraining Labels:")
print(y_train)

print("\nTesting Features:")
print(X_test)

print("\nTesting Labels:")
print(y_test)
```
Answer: Training Features:
[1 8 3 5 4 7]

Training Labels:
[[40][98][60][80][70][95]]

Testing Features:
[2 6]

Testing Labels:
[[50]
 [90]]

### Explanation
- `X` stores the study hours.
- `y` stores the corresponding marks.
- `test_size=0.2` means **20% Testing Data** and **80% Training Data**.
- Since there are **8 rows**, the split becomes:
  - Training Data = **6 rows**
  - Testing Data = **2 rows**
---

## Solution 2 >- Question : Change test_size = 0.2 to test_size = 0.3
### Answer
```python
X_train, X_test, y_train, y_test = train_test_split(    X,y, test_size=0.3, random_state=42)
```
output : 
```text
Training Features:[8 3 5 4 7]
Training Labels:[[98] [60] [80][70][95]]
Testing Features:[2 6 1]
Testing Labels: [[50][90][40]]
```

### Explanation
There are **8 rows** in the dataset.
30% of 8 = **2.4**
Scikit-learn keeps **3 rows** for Testing and **5 rows** for Training.

Result:
```text
Training Data = 5 rows
Testing Data = 3 rows
```

---
## Solution 3-> Question:-  Change random_state = 42 to random_state = 10
### Answer
```python
X_train, X_test, y_train, y_test = train_test_split( X,y,test_size=0.2,random_state=10 )
```
output: 
Training Features:[8 3 5 4 7]
Training Labels:[[98][60][80][70][95]]
Testing Features:[2 6 1]
Testing Labels:[[50][90][40]]

### Explanation
The program still works correctly.However,the Training Data and Testing Data may contain different rows. This happens because a different random seed creates a different shuffle.
Remember:
- `random_state=42` → One fixed shuffle
- `random_state=10` → Another fixed shuffle
Both are correct. Only the selected rows change.

---
## Solution 4 -> Question :- Remove random_state Run the program three times. Does the output remain the same? Why?
### Answer
No. The output does **not** remain the same.

### Reason
Without `random_state`, Scikit-learn shuffles the dataset randomly every time the program runs. Because the data is shuffled differently,different rows may be selected for the Training Data and Testing Data. Therefore,`X_train`, `X_test`, `y_train`, and `y_test` may change every time.

---
### If `random_state=42` is used
The output remains the same every time. Reason: The dataset is shuffled in the same order every time. So,the Training Data and Testing Data remain the same.

---
## Easy Trick to Remember
```text
random_state = Fixed Shuffle
                ↓
            Same Output

No random_state = Random Shuffle
                   ↓
             Different Output
```
---
# Important Questions
1. What is Train/Test Split?
2. Why do we divide the dataset?
3. What is Training Data?
4. What is Testing Data?
5. Which data is used for learning?
6. Which data is used for evaluation?
7. What is the most common Train/Test ratio?
8. What does `test_size` mean?
9. What does `random_state` do?
10. Which Scikit-learn function is used for Train/Test Split?
11. What are `X_train` and `X_test`?
12. What are `y_train` and `y_test`?
13. Why shouldn't we train and test on the same dataset?
14. What happens if `random_state` is removed?
15. Can we use `test_size=0.5`? Why?