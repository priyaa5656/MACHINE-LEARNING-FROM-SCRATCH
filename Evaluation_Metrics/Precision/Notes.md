# What is Precision?
Precision measures the quality of positive predictions. It tells us Out of all Positive Predictions, How many are actually Positive?

## Why Do We Need Precision?
Suppose you built a Machine Learning model. The model predicts Positive Now the question is

How many of those Positive predictions are actually correct?    
This is measured using Precision.

## In Simple Words: 
Precision tells us Out of all the Positive predictions made by the model, how many were actually Positive?       
Precision focuses only on the predictions that the model labeled as Positive.


## Real-Life Example 1 (Disease Detection)
Suppose a hospital tests 100 patients.      
The Machine Learning model predicts 20 Patients → Disease                
But after medical testing, 18 actually have Disease and 2 are Healthy.

The model predicted 20 people as positive, but only 18 were truly positive. This is where Precision is used.


## Why Isn't Accuracy Enough?
Imagine 1000 Patients  → 990 Healthy + 10 Disease     
A model predicts Everyone is Healthy        

Accuracy 990 / 1000 = 99%    
Looks excellent.

But the model failed to detect every diseased patient. Accuracy cannot tell us whether the positive predictions are trustworthy.        
Precision solves this problem.


## In Easy Word :- 
Precision is the percentage of predicted positive cases that are actually positive.


## Real-Life Analogy
Imagine a police officer arrests 10 people.     
After investigation, 8 are Criminals + 2 are Innocent

The officer made 10 positive predictions. Only 8 were correct. Precision measures how accurate those positive decisions were.


----
## Easy Trick
Model says
Positive   → Check   → Actually Positive?   → Precision


----
## Summary
✅ Precision focuses only on Positive Predictions.        
✅ It tells us how trustworthy the model's Positive predictions are.       
✅ High Precision means fewer False Positives.       
✅ Precision is very important in Fraud Detection, Spam Detection, and Medical Diagnosis.


-----
## Problem 1
Suppose a Disease Detection model predicts              
20 Patients   →   Disease       
After medical testing, 18 Actually Disease & 2 Healthy

### Step 1 : Find TP and FP
TP = 18
FP = 2

### Step 2 : Write Formula
                TP
Precision = ----------
              TP + FP

### Step 3 : Put Values
Precision = 18 /18 + 2 = 18 / 20 = 0.90


#### Step 4 : Convert into Percentage
Answer:  0.90 × 100 = 90%

Precision = 90%



## Easy Trick
Model says:
Positive   → Correct   → TP
 
Positive   → Wrong   → FP

---------------
TP / TP + FP   →   Precision


--------
## Summary
✅ Precision uses True Positive (TP) and False Positive (FP).                          
✅ Formula: Precision = TP / (TP + FP)                           
✅ High Precision means fewer False Positives.                  
✅ Precision is very important in Medical Diagnosis, Spam Detection, and Fraud Detection.             


-----------
## What Does Precision Tell Us?
Higher Precision  →  More Correct Positive Predictions  →  Fewer False Positives  →  More Trustworthy Model

Precision measures the reliability of Positive predictions.
If the model says Positive, Precision tells us whether we can trust that prediction or not.

## Example 1
Suppose Precision = 100%

Meaning : Model Predicted 50 Positive   →   All 50 Actually Positive , No False Positives.
FP = 0
This is an ideal situation.

## Example 2
Suppose Precision = 90%
Meaning: Out of every 100 Positive Predictions   →  90 are Correct + 10 are Wrong
The model is highly reliable.

## Example 3
Suppose Precision = 70%
Meaning: Out of every 100 Positive Predictions   →  70 are Correct + 30 are Wrong
The model still makes many False Positive errors.


## Example 4
Suppose Precision = 30%
Meaning: Out of every 100 Positive Predictions  →  30 are Correct + 70 are Wrong
The model is not trustworthy. Most Positive predictions are incorrect.



## Precision Interpretation Table
Precision	|Interpretation
------------|---------------
100%	    |Perfect Positive Predictions
95–99%	    |Excellent
90–94%	    |Very Good
80–89%	    |Good
70–79%	    |Average
Below 70%	|Poor

⚠️ Note:This is a general guideline. for all problem required Precision can be differ.


--------------
## When Do We Need High Precision?
High Precision is important when False Positives are very costly.


Examples
✅ Disease Prediction
Healthy Person  →  Predicted Disease  →  Unnecessary Stress

✅ Spam Detection
Important Email  →  Marked as Spam  →  User Misses Email

✅ Fraud Detection
Normal Transaction  →  Marked Fraud  →  Customer Gets Blocked


------------
## Easy Trick
High Precision  →  Less False Positive  →  Positive Prediction Can Be Trusted

## In one word:- 
Precision tells us how trustworthy the model's Positive predictions are.



## Summary
✅ Precision measures the quality of Positive predictions.                  
✅ Higher Precision means fewer False Positives.                      
✅ High Precision makes Positive predictions more reliable.             
✅ Precision is very important in Medical, Banking, and Spam Detection systems.                 



---------
## Limitation of Precision
### Does High Precision Always Mean a Good Model?
No.

### A model can have 100% Precision and still be a bad model. Why?
Because Precision only looks at Positive Predictions. It completely ignores Actual Positive Cases that the model missed.

### Why Does Precision Fail?
Precision tells us Out of Predicted Positive, How many are Correct?
But it does not tell us How many Positive cases the model failed to detect. That problem is solved by Recall.

🌍 Real-Life Example (Disease Detection)
Suppose 100 Patients  →  20 Actually have Disease + 80 Healthy

Now imagine the model predicts Only 2 Patients  →  Disease            
Those two patients actually have disease. So,                      
TP = 2 , FP = 0          

Now calculate Precision.

Precision = 2 / 2 + 0 = 100%           
Wow! Precision = 100%           

Looks perfect. But What Really Happened? The model found only 2 Patients and completely ignored 18 Diseased Patients.    
Those patients never received treatment. So,

Precision = 100%
❌
Good Medical Model


-----------
### When Is Precision Alone Not Enough?
Precision alone should not be used in               
✅ Disease Detection              
✅ Cancer Prediction               
✅ Fraud Detection                 
✅ Security Systems               
because missing actual Positive cases can be dangerous.


---------
## Summary
✅ High Precision does not always mean a good model.       
✅ Precision ignores missed Positive cases.                
✅ Precision focuses only on Positive Predictions.             
✅ Recall measures how many actual Positive cases were found.             
✅ Precision and Recall should be used together.           


-----------
```python
from sklearn.metrics import precision_score

# Actual Values
y_true = [1,0,1,1,0,1,0,1]


# Predicted Values
y_pred = [1,0,1,0,0,1,1,1]


# Calculate Precision
precision = precision_score(y_true, y_pred)
print("Precision :", precision)
print("Precision Percentage :", precision * 100)
```


-----------
## Explanation of code- 
### Line 1 :- from sklearn.metrics import precision_score
We import the precision_score() function from Scikit-learn. This function automatically calculates the Precision of a Machine Learning model.

In Simple Words:-   Import  →  precision_score()  →  Ready to Calculate Precision


### Line 2: y_true =[1,0,1,1,0,1,0,1]
y_true stores the actual (correct) labels. These are the real answers from the dataset.
Meaning: 1 = Positive , 0 = Negative


### Line 3 : y_pred = [1,0,1,0,0,1,1,1]
y_pred stores the predictions made by the Machine Learning model. These predictions are compared with the actual labels.


### Line 4: precision = precision_score(y_true, y_pred)
precision_score() compares:  Actual Labels  → Predicted Labels

Then it finds 
True Positive (TP)  → Correct Positive Predictions
False Positive (FP)  → Wrong Positive Predictions

Finally it applies Precision =TP/TP + FP

and returns the Precision.

Behind the Scenes Comparison
Actual	|Predicted	|Type
--------|-----------|-----
1	    |1          |✅ TP
0	    |0          |TN
1	    |1          |✅ TP
1	    |0          |FN
0	    |0          |TN
1	    |1          |✅ TP
0	    |1          |❌ FP
1	    |1          |✅ TP


Count
TP = 4 , FP = 1
Formula Precision = 4 / 4 + 1 = 4 / 5 = 0.8


## Line 5: print("Precision :", precision)
Prints the Precision returned by precision_score()                     
Output : Precision : 0.8               


## Line 6: print("Precision Percentage :", precision * 100)
Converts decimal Precision into percentage.                   
Output : 0.8 × 100 = 80%                 


## Complete Workflow
```
Import precision_score()
↓
Store Actual Labels (y_true)
↓
Store Predicted Labels (y_pred)
↓
Compare Both Lists
↓
Find True Positives
↓
Find False Positives
↓
Apply Precision Formula
↓
Return Precision
↓
Print Precision
↓
Convert to Percentage
```


## Real-Life Analogy
Imagine a doctor.The doctor says- Disease for several patients.
Later, lab reports arrive. Now the doctor checks - How many Disease predictions were actually correct?
That is exactly what Precision measures.

Doctor Prediction

↓

Lab Report

↓

Correct Disease Predictions

↓

Precision



## Easy Trick
y_true  →  Actual Answers

y_pred  →  Model Answers

-----------------------
precision_score()  →  TP & FP   →  Precision



--------------
## Important Notes
✅ y_true contains the actual labels.                            
✅ y_pred contains the model predictions.                          
✅ precision_score() internally calculates TP and FP.                         
✅ Output is always between 0 and 1.                                       
✅ Multiply by 100 to convert it into percentage.                                    



## One-Line Definition
precision_score() compares the actual labels with the predicted labels and returns the Precision of the Machine Learning model.


## Summary
✅ Import precision_score().                 
✅ Store actual labels in y_true.               
✅ Store predicted labels in y_pred.        
✅ Use precision_score(y_true, y_pred).    
✅ Multiply by 100 to get the Precision percentage.



## Key Points
✅ Precision focuses only on Positive Predictions.                         
✅ High Precision means fewer False Positives.                      
✅ Precision tells us how trustworthy Positive predictions are.                       
✅ Precision is important when False Positives are costly.                                 
✅ Precision alone is not enough; it should be used with Recall.                           


---------------------
Questions
## Basics
What is Precision?
Why do we use Precision?
What does Precision measure?
Write the Precision formula.
What is True Positive (TP)?
What is False Positive (FP)?
What is the range of Precision?
Can Precision be greater than 100%?
Can Precision be negative?
Is Precision an Evaluation Metric?
Conceptual Questions
What is the meaning of High Precision?
What is the meaning of Low Precision?
Why is Precision important?
Which errors does Precision try to reduce?
Why is Precision important in Disease Detection?
Why is Precision important in Spam Detection?
Why is Precision important in Fraud Detection?
Can a model have 100% Precision and still be bad?
Why?
What is the biggest limitation of Precision?
Python Questions
Which function calculates Precision?
Which library provides precision_score()?
What are y_true and y_pred?
What does precision_score() return?
How do you convert Precision into percentage?
Does precision_score() internally calculate TP and FP?
What happens if there are no Positive predictions?
Can precision_score() work for multiclass classification?
Why should y_true and y_pred have the same length?
Explain the complete Precision workflow in Python.

## Comparison Questions
What is the difference between Accuracy and Precision?
Which metric focuses only on Positive predictions?
Which metric is better for imbalanced datasets?
Can Accuracy be high while Precision is low?
Why do we need Recall if we already have Precision?


## Fill in the Blanks
Question	Answer
Precision uses ______ and ______.	
TP stands for ______.	
FP stands for ______.	
Precision measures the quality of ______ predictions.	
High Precision means fewer ______.	
precision_score() belongs to ______.	
Precision is usually written as a ______.	
Precision focuses only on ______ predictions.	
Precision is very useful in ______ Detection.	
Precision is always between ______ and ______.	

## True / False
Precision is an Evaluation Metric. ( )
Precision uses TP and FP. ( )
High Precision means fewer False Positives. ( )
Precision measures all predictions. ( )
Precision is important in Spam Detection. ( )
Precision alone is enough to evaluate every model. ( )
precision_score() is available in Scikit-learn. ( )
Precision can never exceed 100%. ( )
High Precision always means the model is perfect. ( )
Precision and Recall are usually used together. ( )