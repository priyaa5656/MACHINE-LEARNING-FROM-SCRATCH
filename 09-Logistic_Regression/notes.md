# Logistic Regression

## 🤔 What is Logistic Regression?
Logistic Regression is a **Supervised Machine Learning Classification Algorithm** used to predict **categories (classes)** instead of continuous numerical values.

In simple words, Logistic Regression predicts **which class an input belongs to.**


---
## 📖 Simple words
Linear Regression predicts **numbers**. Logistic Regression predicts **categories**.


---
## 🌍 Real-Life Examples
### Example 1
Student Studies

↓

Pass or Fail


### Example 2
Email

↓

Spam or Not Spam


### Example 3
Patient

↓

Disease or Healthy


## Example 4
Image

↓

Cat or Dog


---
## Why Can't Linear Regression Solve These Problems?
Suppose we want to predict
```text
Pass or Fail

We assign:- Pass = 1 , Fail = 0

Now imagine Linear Regression predicts

```text
0.27
or
1.45
or
-0.60
```

But our answer should only be
```text
0 or 1
```

Linear Regression can produce **any number**, so it is not suitable for classification.


---
## Problem with Linear Regression
```text
Prediction
↓
2.3 ❌
-1.8 ❌
0.65 ❌
```

We only need 0 or 1.

Therefore, Linear Regression is **not suitable for Classification Problems.**


---
## What Does Logistic Regression Predict?
Instead of predicting a number, it predicts a **Probability**.

Example-        
Probability = 0.92

Meaning 92% Chance of Passing



Another example:-            
Probability = 0.15

Meaning 15% Chance of Passing


---
## How Does Logistic Regression Decide?

Usually,

```text
Probability ≥ 0.5
↓
Class = 1


Probability < 0.5
↓
Class = 0
```
This value (0.5) is called the **Decision Threshold**.


---
### Example
```
Probability = 0.95
↓
Pass


Probability= 0.80
↓
Pass


Probability = 0.42
↓
Fail


Probability = 0.10
↓
Fail
```

---
## Easy Real-Life Example
Imagine a weather app.

###
It says Chance of Rain = 95%

You will probably carry an umbrella.

---
###
If it says Chance of Rain = 10%

You probably won't carry one.

Logistic Regression works in the same way. It predicts the **probability** first, then converts it into a class.



---
## Easy Trick
```text
Linear Regression
↓
Predicts Numbers


---------------------


Logistic Regression
↓
Predicts Probability
↓
Converts into Class
```

---
## One-Line Definition
Logistic Regression is a Supervised Machine Learning algorithm used for Classification by predicting probabilities and converting them into classes.

---
## Summary
✅ Used for Classification.       
✅ Predicts Probability.        
✅ Output lies between 0 and 1.       
✅ Converts probability into classes.    
✅ Solves Binary Classification problems.



## Why is it Called Logistic Regression?
---
## 🤔 The Biggest Confusion
Many beginners think,

```text
Linear Regression
↓
Regression
↓
Predict Numbers
```

So,
```text
Logistic Regression
↓
Should Predict Numbers?
❌ Wrong.
```
Even though its name contains **Regression**, it is actually a **Classification Algorithm**.


---
## Why is the Name "Regression"?
The word **Regression** comes from the mathematical model it uses. Logistic Regression first calculates a value using a **Linear Regression equation**.
```text
z = w₁x₁ + w₂x₂ + ... + b
```
This equation is exactly the same type of equation used in Linear Regression.

### Step 1
First, Logistic Regression calculates z using a linear equation.

Example:- 

```text
Study Hours = 6
↓
Linear Equation
↓
z = 2.7
```
Notice, This is **not the final answer.**


### Step 2
Now this value z = 2.7

is passed into a special function called the `Sigmoid Function`.


### Step 3
Sigmoid converts

```text
2.7
↓
0.937
```
Now the output becomes a probability.


### Step 4
Finally,
```text
0.937
↓
93.7%

Since 93.7% > 50%

Prediction becomes

PASS
```

---

## Complete Workflow
```text
Input
↓
Linear Equation
↓
z
↓
Sigmoid Function
↓
Probability
↓
Class
```

---
## Why Isn't It Called Logistic Classification?
Historically, the mathematical model was developed using **Regression equations**.           
Later, the output was converted into probabilities using the **Logistic (Sigmoid) Function**.         
That's why the name became `Logistic + Regression`          

The word **Logistic** comes from the **Logistic (Sigmoid) Function**.      
The word **Regression** comes from the **Linear Regression equation**.       
Together, **`Linear Equation + Sigmoid Function = Logistic Regression`**


---
## Real-Life Analogy
Imagine a school teacher.

### Step 1- The teacher calculates total marks.
Math + Science + English => Total = 82

### Step 2- School Rule : Above 40 = PASS ,  Below 40 = FAIL
The calculation uses numbers, but the final result is a category. Exactly the same happens in Logistic Regression.

---


---
## One-Line Definition
Logistic Regression is called "Regression" because it uses a Regression equation internally, but its final goal is Classification.

---
## Summary
✅ Uses a Linear Equation internally.        
✅ Uses the Sigmoid Function.           
✅ Predicts Probability.          
✅ Converts Probability into Class.             
✅ Therefore it is a Classification algorithm.



---
## 🤔 What is Classification?
Classification is a Machine Learning task in which the model predicts **categories (classes)** instead of numerical values.               
In simple words,Classification is the process of predicting the correct class or category for a given input. 


---
## Real-Life Analogy
Imagine a teacher checking exam results. The teacher doesn't always write exact marks.

Sometimes the teacher only writes Pass or Fail . This is Classification.

Now imagine another teacher writes ( Marks = 82 ).  This is Regression.


---
## How Classification Works
```text
Input Data
↓
Model Learns Patterns
↓
New Data
↓
Predict Category
```

---
Example-  Training Data
```text
Study Hours |Result|
------------|------|
1           | Fail |
2           |  Fail|
5           | Pass |
8           |Pass  |
```

```
New Student Study Hours = 6
↓
Prediction
↓
Pass
```

---
## summry 
```
Regression
↓
Predicts Continuous Numerical Values

Example House Price = ₹50 Lakhs

--------------------------

Classification
↓
Predicts Categories

Example- Spam / Not Spam
```


---
## 🤔 What are the Types of Classification?
Classification problems are mainly divided into **three types**.Each type is used for different kinds of prediction problems.
```text
Classification
    |
    ├──────────────>  1. Binary Classification
    | 
    |
    ├──────────────>  2. Multi-Class Classification
    |
    |
    ├──────────────>  3. Multi-Label Classification
    |
```


---
### 1. Binary Classification
Binary means **Two**. In Binary Classification, there are only **two possible classes**.
Like - 
YES or NO      
0 or 1        
True or False


---
#### Real-Life Examples

##### Medical Test
Disease or Healthy

##### Loan
Approved or Rejected

##### Transaction
Fraud or Not Fraud


---
#### Binary Classification Diagram
```text
Input
↓
Model
↓
Pass or Fail
```

---
#### Easy Trick
```text
Binary
↓
Bi
↓
2 Classes
```


---
### 2. Multi-Class Classification
Multi means **Many**.    
In Multi-Class Classification, one input belongs to **only one class**, but there are **more than two classes**.


---
#### Real-Life Examples
Animal Image
```text
Cat

Dog

Horse

Cow
```
Only one answer will be correct.

---
Fruit

```text
Apple

Banana

Orange

Mango
```
Only one fruit.


---
#### Multi-Class Diagram
```text
Input
↓
Model
↓
Cat / Dog / Horse/Cow
↓
Only One Output
```

---
## Easy Trick

```text
Multi
↓
Many Classes
↓
Only One Correct Answer
```

---
### 3. Multi-Label Classification
In Multi-Label Classification, one input can belong to **multiple classes at the same time**.

---
#### Real-Life Examples
Movie
```text
Action

Comedy

Adventure
```
One movie can have all three labels.

---
Photo

```text
Person

Car

Tree

Dog
```
One image can contain all of them.

---

Music

```text
Romantic

Sad

Slow
```
A single song can have multiple labels.

---
### Multi-Label Diagram
```text
Input

↓

Model

↓

Action

Comedy

Adventure

↓

Multiple Outputs
```

---
## Comparison
| Feature           | Binary    | Multi-Class   | Multi-Label     |
|------------------ |-----------|---------------|-----------------|
| Number of Classes | 2         | More than 2   | More than 2     |
| One Output?       | yes       | ✅            | ❌             |
| Multiple Outputs? | No        | ❌            | ✅             |
| Example           | Pass/Fail | Cat/Dog/Horse | Action + Comedy |

---
### Real-Life Comparison
Exam Result = Pass / Fail

↓

Binary

----------------------------
Animal Image
```text
Cat
Dog
Horse
```

↓

Multi-Class

----------------------------
Movie Genres
```text
Action
Comedy
Romance
```

↓

Multi-Label

---
### Easy Trick
```text
Binary
↓
2 Classes


-----------------

Multi-Class
↓
Many Classes
↓
One Correct


-----------------

Multi-Label
↓
Many Classes
↓
Many Correct
```

---
## One-Line Definitions
Binary Classification - Predicts one of two classes.

---
Multi-Class Classification - Predicts one class from many classes.

---
Multi-Label Classification - Predicts multiple classes for one input.

---
## Summary
✅ Binary = 2 Classes         
✅ Multi-Class = Many Classes but One Output       
✅ Multi-Label = Many Classes and Multiple Outputs


---
## Summary
✅ LogisticRegression() creates the model.           
✅ fit() trains the model.           
✅ predict() predicts the class.         
✅ predict_proba() predicts probabilities.          
✅ Output class is usually     
0 = Fail  / 1 = Pass


# Homework

## Question 1: Predict for [[2]]. What is the output?
```python
prediction = model.predict([[2]])
print(prediction)
# Output- [0]
```
Meaning : 0 = Fail

---

## Question 2 : Predict for [[8]]. What is the output?
[1] = Pass

---

## Question 3: Print predict_proba([[2]]). Observe the probabilities.
```python
probability = model.predict_proba([[2]])
print(probability)
```
Example Output: [[0.89 0.11]]       
Interpretation: 89% Fail,  11% Pass     
⚠️ Note: your exact numbers may me different , because this is depend on model training.

---

---

## Question 4: Create your own dataset.Train Logistic Regression.
```python
import numpy as np

from sklearn.linear_model import LogisticRegression

X = np.array([
    [16],
    [18],
    [20],
    [25]
])

y = np.array([
    0,
    0,
    1,
    1
])

model = LogisticRegression()

model.fit(X, y)

prediction = model.predict([[22]])

print("Prediction :", prediction)

probability = model.predict_proba([[22]])

print("Probability :", probability)
```


## Logistic Regression (Unique Questions)
What is Logistic Regression?
Is Logistic Regression a Regression or Classification algorithm?
What type of problems does Logistic Regression solve?
Why can't Linear Regression solve Classification problems?
What does Logistic Regression predict?
What is Probability?
What is the output range of Logistic Regression?
What is the Decision Threshold?
Give one real-life example of Logistic Regression.
Why is Logistic Regression called Regression?
What does Logistic Regression calculate first?
What is the role of the Linear Equation?
What is the role of the Sigmoid Function?
What is the final output of Logistic Regression?
Why isn't Logistic Regression called Logistic Classification?
What does the word "Logistic" mean?
Explain the complete workflow of Logistic Regression.
What is the difference between Linear Regression and Logistic Regression?

## Classification (Unique Questions)
What is Classification?
What does a Classification model predict?
What is the difference between Regression and Classification?
Give three real-life examples of Classification.
Is Spam Detection a Classification problem?
Is House Price Prediction a Classification problem?
Is Disease Prediction a Classification problem?
What are the main types of Classification?
Why is Classification important?
Give one real-life analogy for Classification.

## Types of Classification (Unique Questions)
What is Binary Classification?
What is Multi-Class Classification?
What is Multi-Label Classification?
Give two examples of Binary Classification.
Give two examples of Multi-Class Classification.
Give two examples of Multi-Label Classification.
How many classes are there in Binary Classification?
Can Multi-Class Classification have multiple outputs?
Can Multi-Label Classification have multiple outputs?
What is the biggest difference between Multi-Class and Multi-Label Classification?
Which type of classification is used in Pass/Fail prediction?
Which type of classification is used in Cat/Dog/Horse prediction?
Which type of classification is used in Movie Genre prediction (Action + Comedy + Drama)?
Can Logistic Regression solve Binary Classification?
Can Logistic Regression solve Multi-Class Classification?
Can basic Logistic Regression directly solve Multi-Label Classification?