# AI vs Machine Learning vs Deep Learning

First understand this:- 
Artificial Intelligence (AI)
├── Machine Learning (ML)
│      └── Deep Learning (DL)


## Artificial Intelligence (AI)
AI means making a machine intelligent.
AI = Teaching a machine to think and make decisions like a human.

Examples:
ChatGPT
Self-driving car
Chess-playing robot
Siri
Alexa

## Machine Learning (ML):
Machine Learning is a subset of AI. Here, the programmer does not write every single rule; instead, the machine learns patterns by analyzing data on its own.

### Example1 :-  Spam Email
Old Method
IF subject contains "Win Money and Free"
Spam
ELSE
Not Spam

New Method
Show the machine a million emails. It will learn on its own what the pattern of a spam email looks like.

### Example 2 :- Netflix
You watch horror movies.
↓
Netflix recommends more horror movies. This is Machine Learning.


## Deep Learning (DL):-
Deep Learning is an advanced version of ML. It uses neural networks, similar to the human brain. This enables...
Face Recognition
ChatGPT
Gemini
Image Generation
Speech Recognition

### Simple Example
Imagine you have a child—AI.
The child is intelligent—ML.

The child learns by looking at examples:
Dog
Dog
Dog
↓
This is a dog.

Deep Learning: The child begins to understand automatically after seeing millions of images.

## In simple terms:
AI = Making the machine intelligent.
ML = The machine learning from data.
DL = The machine learning via Neural Networks.


## Types of Machine Learning
you have to be remembered Only 4 type of Machine Learning
1. Supervised Learning
2. Unsupervised Learning
3. Reinforcement Learning
4. Semi-Supervised Learning


### (1) Supervised Learning
Most important. The answer is also given along with the data.
Example :- House Size
1000 sqft → ₹20 lakh
1500 sqft → ₹30 lakh
1800 sqft → ₹40 lakh
Now the machine will read. and predict answer

1300 sqft
↓
Predict ₹25 lakh
This is Supervised Learning.

Example
House Price Prediction
Salary Prediction
Student Result Prediction
Spam Detection


### (2) Unsupervised Learning
No manual input was provided. The machine creates the groups itself.
Example : Shopping Data
Person A
Pizza
Burger
Fries
↓
Food Lover

The machine automatically forms the clusters.

Example
Customer Segmentation


### (3) Reinforcement Learning

Machines learn from rewards and punishments.
Example
Chess AI
Win + 10 Reward
Lose - 10
Slowly learns the best moves.

Example
Self-Driving Cars
Robotics
Game-Playing AI

### (4) Semi-Supervised Learning
Some labeled, some unlabeled
Both mixed.

## Trick to remember
Supervised- Teacher gives the answer.
Unsupervised-Form your own group.
Reinforcement-Learn from rewards.
Semi-Half answer.


## Machine Learning Workflow
Every ML project roughly follows this flow:
Problem 
↓
Collect Data 
↓
Clean Data 
↓
Feature Engineering 
↓
Train Model 
↓
evaluate 
↓
Deploy 
↓
prediction

Example: House Price Prediction
Problem → House price predict karna.
Collect Data → Area, rooms, location, age.
Clean Data → Missing values, remove duplicates.
Feature Engineering → Creating useful features.
Train Model → Learning the model from data.
Evaluate → Accuracy check.
Deploy → Use in Website/App.
Prediction → The price of the new house.


6. Common Terminology
Dataset

Poora data.

Example:

Area	Rooms	Price
1000	2	20L
1500	3	30L
Feature (X)

Input.

Example:

Area
Rooms
Age
Label / Target (y)

Output.

Example:

Price
Training Data

Model isi data se seekhta hai.

Test Data

Model ko exam dene ke liye.

Model

Jo patterns seekhta hai.

Example:

Linear Regression

Decision Tree

Random Forest
Prediction

Model ka answer.

Ek Simple Diagram
Features (X)

Area

Rooms

Age

↓

Model

↓

Prediction (y)

Price
7. First Scikit-learn Program 🎉

Ye tumhara pehla ML program hoga.

from sklearn.linear_model import LinearRegression
import numpy as np

# Features (House Area)
X = np.array([[1000], [1500], [2000]])

# Labels (House Price in Lakhs)
y = np.array([20, 30, 40])

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Price of 1800 sqft house
prediction = model.predict([[1800]])

print("Predicted Price:", prediction[0], "Lakhs")
Output (approx.)
Predicted Price: 36.0 Lakhs
Is code me kya hua?
X → Input (house area)
y → Output (price)
LinearRegression() → Model banaya
fit() → Model ko train kiya
predict() → Naye house ka price predict kiya