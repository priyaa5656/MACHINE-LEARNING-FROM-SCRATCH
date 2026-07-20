# Why Do We Need Accuracy?
Imagine you build a Machine Learning model. Now the model starts making predictions.

The next question is: Are the predictions correct? How do we measure that?
We use Accuracy.

In Simple Words: Accuracy tells us how many predictions made by the model are correct.        
It is one of the simplest ways to measure the performance of a Machine Learning model.


---
## Real-Life Example 1
Suppose there are 100 students. The model predicts
90 students correctly       
10 students incorrectly

Then Accuracy = 90%       
The model is 90% accurate.


## Real-Life Example 2 - Weather Prediction
Today's Prediction → Rain       
Actually, Rain happened       
✅ Correct Prediction        
Suppose Out of 30 days, the weather app predicted correctly on 27 days.      
Accuracy = 27 / 30 => 90%



##  Why Can't We Just Look at Predictions?
Suppose a model predicts

Pass

Pass

Pass

Pass

Pass

Is the model good?
Maybe /Maybe not.

> We need a numerical value to compare different models. That numerical value is called Accuracy.


## What is Accuracy?
Accuracy is the percentage of correct predictions made by a Machine Learning model.      
It compares Correct Predictions → Total Predictions
Accuracy is the ratio of correct predictions to the total number of predictions made by the model.

---
## Easy Trick
More Correct Predictions →  Higher Accuracy →  Better Model
One-Line Definition


---
## Summary
✅ Measures model performance.    
✅ Counts correct predictions.     
✅ Expressed as a percentage.    
✅ Higher Accuracy usually means a better model.


## Accuracy Formula
Accuracy tells us how many predictions made by the model are correct out of all predictions. It is calculated using a simple formula.

Formula
```
                Correct Predictions
Accuracy = ---------------------------- × 100
               Total Predictions
```

Formula Meaning:- 

Correct Predictions     
Means - The number of predictions that are correct.

Total Predictions    
Means - All predictions made by the model.

Correct + Wrong Predictions


## Real-Life Example 1
Suppose
Total Students = 100   
Correct Predictions = 92     
Wrong Predictions = 8

Then    
Accuracy = 92 / 100 × 100 = 92%

The model has 92% Accuracy.


## Easy Trick
Correct Predictions → Divide → Total Predictions → Multiply by 100 → Accuracy


---
## Summary 
✅ Accuracy measures model performance.     
✅ Formula uses Correct Predictions and Total Predictions.     
✅ Answer is always expressed as a percentage.     
✅ Higher Accuracy usually means better performance.




----
## Problem:- 
Suppose a Machine Learning model made 100 predictions.
Correct Predictions = 95
Wrong Predictions = 5

### Step 1 : Write the Formula

                Correct Predictions
Accuracy = ---------------------------- × 100
               Total Predictions


### Step 2 : Find Total Predictions
Correct + Wrong
95 + 5 = 100

### Step 3 : Put the Values
Accuracy = 95 / 100 × 100 = 95%

Answer -> Accuracy = 95%


## 🌍 Real-Life Example
Imagine a teacher checks 50 answer sheets.
Correctly Checked = 47
Wrongly Checked = 3
Accuracy = 47 / 50 × 100 = 94%
The teacher's checking accuracy is 94%.



## Easy Trick
Correct Predictions

↓

Correct + Wrong

↓

Multiply by 100

↓

Accuracy



## Summary         
✅ Accuracy = Correct Predictions ÷ Total Predictions × 100         
✅ Total Predictions = Correct + Wrong         
✅ Higher Accuracy means the model makes more correct predictions.



## What Does Accuracy Tell Us?
Accuracy tells us how often the Machine Learning model predicts correctly.

In simple words,

Higher Accuracy

↓

More Correct Predictions

↓

Better Model (Usually)



## Simple Definition-
Accuracy represents the overall correctness of a Machine Learning model.

### Example 1:  Suppose Accuracy = 98%
Meaning: Out of every 100 predictions, 98 are correct 2 are wrong. This is usually considered a very good model.


### Example 2: Suppose Accuracy = 10%
Meaning Out of every 100 predictions, 10 are correct 90 are wrong.
This is a poor model.

#### Accuracy Interpretation Table
Accuracy	| Interpretation
100%	    |Perfect Model
Below 70%	|Poor (depends on the problem)

⚠️ Note: This is a general guideline. for all problem there is no fixed rule.


#### Hospital Example
Suppose a disease prediction model has Accuracy = 99%
Sounds amazing? Maybe. Maybe not.
If the model misses the 1% who actually have a dangerous disease, that can be a serious problem.
So, High Accuracy ≠ Always Best Model



##### Important Note: Accuracy is a good metric when Classes are balanced.
Example: Pass = 50 Students    
Fail = 50 Students

In this case, Accuracy gives a reliable idea of model performance.

Accuracy tells us the overall percentage of correct predictions made by a Machine Learning model.


## Summary
✅ Accuracy measures overall correctness.      
✅ Higher Accuracy usually means better performance.      
✅ 100% Accuracy means every prediction is correct.      
✅ High Accuracy does not always mean the best model.   
✅ For important applications (medical, fraud detection, spam filtering), we also use Precision, Recall, and F1 Score.



## Limitation of Accuracy
Does High Accuracy Always Mean a Good Model?
No.A model can have very high Accuracy but still make bad predictions. This usually happens when the dataset is imbalanced.

Accuracy only tells us how many predictions are correct.It does not tell us which type of mistakes the model is making.

## What is an Imbalanced Dataset?
An Imbalanced Dataset is a dataset where one class has many more samples than the other class.


### Real-Life Example (Hospital)

Suppose a hospital has 1000 Patients  →  990 Healthy + 10 Disease

Now imagine the model predicts Everyone is Healthy

Prediction Healthy = 1000 , Disease = 0

Is the Model Correct?
Correct Predictions 990
Wrong Predictions 10

Calculate Accuracy
Accuracy = 990 / 1000 × 100 = 99%

Wow! Accuracy = 99%
Looks amazing... 
But.The model failed to detect every diseased patient.

### Why Is This Dangerous?
Imagine those 10 patients actually have cancer.

The model says Healthy, Those patients may never receive treatment.

So,99% Accuracy ❌ Good Medical Model


### Why Does Accuracy Fail?
Accuracy counts only Correct and Wrong.
It does not tell us Which class was predicted incorrectly.

#### Easy Comparison
> Balanced Dataset      
Pass = 50        
Fail = 50     
Accuracy works well.

> Imbalanced Dataset
Healthy = 990     
Disease = 10     
Accuracy becomes misleading.

### When Should We Avoid Accuracy?
Accuracy alone should not be used for     
✅ Disease Detection     
✅ Fraud Detection     
✅ Spam Detection     
✅ Credit Card Fraud     
✅ Security Systems
These problems usually have imbalanced datasets.



## Easy Trick
Balanced Dataset

↓

Accuracy is Useful

-------------------------

Imbalanced Dataset

↓

Accuracy Can Mislead


## One-Line :-
Accuracy is not a reliable metric for imbalanced datasets because it can give a high score even when the model fails to detect the important class.


## Summary
✅ Accuracy measures overall correctness.       
✅ High Accuracy does not always mean a good model.       
✅ Accuracy can be misleading for imbalanced datasets.       
✅ Medical, fraud, and spam detection problems should not rely only on Accuracy.     
✅ Precision, Recall, and F1 Score solve this problem.



```python
from sklearn.metrics import accuracy_score

# Actual Values
y_true = [1,0,1,1,0,1,0,1]

# Predicted Values
y_pred = [1,0,1,0, 0 ,1,0,1]

# Accuracy
accuracy = accuracy_score(y_true, y_pred)

print("Accuracy :", accuracy)

print("Accuracy Percentage :", accuracy * 100)

```


### Line-by-Line Explanation

#### Line 1 : from sklearn.metrics import accuracy_score
We import the accuracy_score() function from Scikit-learn.
This function automatically calculates the Accuracy of a Machine Learning model.


#### Line 2:  y_true = [1,0,1,1,0,1,0,1]
y_true stores the actual (correct) answers. These are the real labels from the dataset.     
Meaning:-   1 = Pass  , 0 = Fail

#### Line 3: y_pred = [1,0,1,0,0,1,0,1]
y_pred stores the predictions made by the Machine Learning model. These values are compared with y_true.

#### Line 4:  accuracy = accuracy_score(y_true, y_pred)
This is the most important line. accuracy_score() function compares                     
Actual Values → Predicted Values

It counts Correct Predictions and Wrong Predictions

Then applies Accuracy = Correct Predictions / Total Predictions

Finally, it returns the Accuracy.

Behind the Scenes
```
Actual |Prediction  |Comparison
-------|------------|--------|
1      |   1        |  y     |
0      |   0        |  y     |
1      |   1        |  y     |
1      |   0        |  no    |
0      |   0        |   y    |
1      |   1        |  y     |
0      |   0        |  y     |
1      |   1        |  y     |
```
Correct = 7    
Total = 8



### Line 5:  print("Accuracy :", accuracy)
Prints the Accuracy returned by accuracy_score().

Output
Accuracy = 7 / 8 = 0.875   

### Line 6 : print("Accuracy Percentage :", accuracy * 100)
We multiply Accuracy by 100 to convert it into percentage.     
because Accuracy is returned in decimal form.          
Output     
Accuracy Percentage :    0.875 ×100 = 87.5%


## Complete Workflow
Import accuracy_score()

↓

Store Actual Values (y_true)

↓

Store Predicted Values (y_pred)

↓

Compare Both Lists

↓

Count Correct Predictions

↓

Apply Accuracy Formula

↓

Return Accuracy

↓

Print Accuracy

↓

Convert to Percentage


---
## ⚠️ Important Notes
✅ y_true must contain the actual labels.                
✅ y_pred must contain the model predictions.                      
✅ Both lists must have the same number of values.                             
❌ If their lengths are different, Python will raise an error.                 


## Key Points
✅ Accuracy measures overall model performance.       
✅ Higher Accuracy usually means better performance.       
✅ Accuracy is expressed as a percentage.       
✅ Uses Correct Predictions and Total Predictions.       
✅ Accuracy alone is not reliable for imbalanced datasets.    
✅ Medical, Fraud Detection and Spam Detection usually require Precision, Recall and F1 Score.


Questions

## Basics
What is Accuracy?
Why do we use Accuracy?
What does Accuracy measure?
What is the formula for Accuracy?
What are Correct Predictions?
What are Total Predictions?
Is Accuracy an Evaluation Metric?
Can Accuracy be greater than 100%?
Can Accuracy be negative?
What is the range of Accuracy?

## Conceptual Questions
Does higher Accuracy always mean a better model?
What is an imbalanced dataset?
Why does Accuracy fail on imbalanced datasets?
Give one example where Accuracy is misleading.
Why isn't Accuracy suitable for Disease Detection?
Why isn't Accuracy suitable for Fraud Detection?
Which metrics should we use instead of Accuracy?
What is the difference between Accuracy and Precision?
What is the difference between Accuracy and Recall?
When should we use Accuracy?

## Python Questions
Which library provides accuracy_score()?
Which module contains accuracy_score()?
What does accuracy_score() return?
What are y_true and y_pred?
Why should y_true and y_pred have the same length?
How do you convert Accuracy into percentage?
Can accuracy_score() work for multiclass classification?
What happens if predictions are completely wrong?
What is the output type of accuracy_score()?
Explain the Accuracy workflow in Python.
What will happen if len(y_true) != len(y_pred)



## Fill in the Blanks
Question	Answer
Accuracy measures ______ predictions.	
Accuracy is an ______ metric.	
Higher Accuracy usually means a ______ model.	
Accuracy is calculated using ______ Predictions and Total Predictions.	
accuracy_score() belongs to ______.	
Accuracy is usually written as a ______.	
Accuracy can be misleading on ______ datasets.	
y_true stores ______ values.	
y_pred stores ______ values.	
Accuracy is always between ______ and ______.	

## True / False
Accuracy is an Evaluation Metric. ( )
Accuracy is always enough to evaluate every model. ( )
Accuracy can be misleading on imbalanced datasets. ( )
accuracy_score() is available in Scikit-learn. ( )
Accuracy is expressed as a percentage. ( )
Higher Accuracy always means the perfect model. ( )
Disease Detection should rely only on Accuracy. ( )
y_true contains actual labels. ( )
y_pred contains predicted labels. ( )
Accuracy can never exceed 100%. ( )