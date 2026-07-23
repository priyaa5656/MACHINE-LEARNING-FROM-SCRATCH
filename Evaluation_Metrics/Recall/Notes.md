# what is Recall?
Recall tells us "Out of all the actual Positive cases, how many were correctly identified by the model?" 
Recall focuses on finding every Positive case.

## Why Do We Need Recall?
Suppose a Machine Learning model is used to detect Disease. The question is NOT , How many Positive Predictions are Correct?
> Instead the question is " Out of all Actual Disease Patients, How many did the model detect? This is measured using Recall.

-------------
## Real-Life Example 
Imagine a police officer searching for 100 Criminals . The officer catches 95 Criminals , Misses 5 Criminals
Recall tells us Out of all Criminals, How many were caught?
High Recall means Very Few Patients are Missed.



##  Summary
✅ Recall focuses on Actual Positive cases.                           
✅ It tells us how many Positive cases the model found.                     
✅ High Recall means fewer missed Positive cases.              
✅ Recall is very important in Disease Detection, Cancer Detection, and Fraud Detection.          



---------
## What Does Recall Measure?
Recall tells us Out of all the Actual Positive cases, how many were correctly identified by the model?

## Why Do We Need Recall Formula?
Suppose there are 100 Patients         
Actually 20 Patients → Disease                     
The model predicts 18 Patients → Disease                    
It misses → 2 Patients                              
Now we want to calculate "How many Diseased Patients were found?"  For this, we use Recall.


-------------
## Formula

                  True Positive
Recall =  -------------------------------
          True Positive + False Negative


Or simply, Recall = TP / (TP + FN)


### What is TP?
True Positive (TP) = Actually Positive → Predicted Positive

Example: 
Patient has Disease → Model says Disease


### What is FN?
False Negative (FN) = Actually Positive → Predicted Negative

Example
Patient has Disease  →  Model says Healthy ❌ Wrong

This is called a Missed Positive Case.


##  Disease Example
Suppose 20 Patients Actually have Disease            
Model finds  →  18 Patients have disease           
Misses  →  2 Patients                   

So, TP = 18 , FN = 2           
Apply Formula:  Recall = 18 / 18 + 2 = 18 / 20 = 0.90

Convert into Percentage   
0.90 × 100 = 90%

Easy Trick: 
Actual Positive  →  Found  →  TP          
Actual Positive  →  Missed  →  FN             
TP / TP + FN  →  Recall              


🎯 Easy Memory Trick
Precision  →  Predicted Positive  →  FP              
Recall  →  Actual Positive  →  FN               


## Summary
✅ Recall uses True Positive (TP) and False Negative (FN).                                 
✅ Formula: Recall = TP / (TP + FN)                         
✅ High Recall means fewer missed Positive cases.                  
✅ Recall is very important in Disease Detection, Cancer Detection, and Fraud Detection.                   


----------------
In simple words,
Higher Recall  →  More Actual Positive Cases Found  →  Fewer False Negatives  →  Less Chance of Missing Important Cases


## Simple Word:-
Recall measures the model's ability to find all Actual Positive cases. If there are Positive cases in the dataset,
Recall tells us How many were successfully found by the model.


### Example 1: 
Suppose Recall = 70%

Meaning:- Out of every 100 Actual Positive Cases   →  70 Found + 30 Missed
>Many Positive cases are still missed.

### Example 2:
Suppose Recall = 30%     

Meaning:- Out of every 100 Actual Positive Cases  →  30 Found + 70 Missed                     
>Very poor Recall. The model misses most Positive cases.                   



## Recall Interpretation Table
Recall	    |Interpretation
------------|----------------
100%	    |Perfect Recall
95–99%	    |Excellent
90–94%	    |Very Good
80–89%	    |Good
70–79%	    |Average
Below 70%	|Poor



## When Do We Need High Recall?
High Recall is important when Missing a Positive case is very dangerous.

### Real-Life Analogy
Imagine a firefighter searching a building.
There are 100 People 
The firefighter = rescues  →  98 People 
Misses  →  2 People

Recall tells us Out of all People, How many were rescued?



-------------
## Limitation of Recall

### Does High Recall Always Mean a Good Model?
No.

### A model can have 100% Recall and still be a bad model. Why?
Because Recall only tries to find all Actual Positive cases. It doesn't care how many False Positives it creates.

📖 In Simple World:-  
Recall tells us Out of all Actual Positive Cases,How many were found? But Recall does not tell us How many Healthy cases were incorrectly predicted as Positive. That problem is solved by Precision.


## When Is Recall Alone Not Enough?
Recall alone should not be used in      
✅ Spam Detection       
✅ Face Unlock       
✅ Email Filtering       
✅ Recommendation Systems           
because too many False Positives create problems.


## Summary
✅ High Recall does not always mean a good model.                        
✅ Recall ignores False Positives.                             
✅ Recall focuses only on Actual Positive cases.                                
✅ Precision measures how many Positive predictions are actually correct.                   
✅ Precision and Recall should always be used together.                         


------------------
```python 
Complete Program
from sklearn.metrics import recall_score

y_true = [1,0,1,1,0,1,0,1]
   
y_pred = [1,0,1,0,0,1,1,1]
  

recall = recall_score(y_true, y_pred)
print("Recall :", recall)
print("Recall Percentage :", recall * 100)
#Output: Recall : 0.8 , Recall Percentage : 80.0
```

-----------------
🔍 Line-by-Line Explanation
### Line 1: from sklearn.metrics import recall_score
We import the recall_score() function from Scikit-learn.       
This function automatically calculates the Recall of a Machine Learning model.

### Line 2: y_true = [1,0,1,1,0,1,0,1]
y_true stores the actual (correct) labels. These are the real answers from the dataset.           
Meaning: 1 = Positive , 0 = Negative


### Line 3: y_pred = [1,0,1,0,0,1,1,1]
y_pred stores the predictions made by the Machine Learning model.      
These predictions are compared with the actual labels.

### Line 4: recall = recall_score(y_true, y_pred)
recall_score() compares Actual Labels  →  Predicted Labels

Then it finds
True Positive (TP)  →  Correct Positive Predictions
False Negative (FN)  →  Positive Cases

Missed by the Model

Finally it applies Recall =TP/TP + FN

🧮 How Did It Calculate 80%? Let's compare both lists.
Actual (y_true)	|Predicted (y_pred) |Result
----------------|-------------------|---------     
1	            |1	                |✅ TP
0	            |0	                |TN
1	            |1	                |✅ TP
1	            |0	                |❌ FN
0	            |0	                |TN
1	            |1	                |✅ TP
0	            |1	                |FP
1	            |1	                |✅ TP

Step 1 : Count True Positives
TP = 4
Step 2 : Count False Negatives
FN = 1
Step 3 : Apply Formula
Recall = TP / TP + FN 
=4/ 4 + 1 = 4 / 5 = 0.8


### Line 5:print("Recall :", recall)
Prints the Recall returned by recall_score()
Output: Recall : 0.8

### Line 6: print("Recall Percentage :", recall * 100)
Converts decimal Recall into percentage.
0.8 × 100 = 80%

----------------
## Important Notes
✅ y_true contains the actual labels.                            
✅ y_pred contains the model predictions.                           
✅ recall_score() internally calculates TP and FN.                               
✅ Output is always between 0 and 1.                                        
✅ Multiply by 100 to convert it into percentage.                 



------------------------
## Workflow
Actual Values (y_true)  →  Predicted Values (y_pred)  →  recall_score()  →  True Positive Count  →  False Negative Count  →  Recall  →  Percentage

```
--------------
## Key Points
Recall focuses on Actual Positive cases.
High Recall means fewer False Negatives.
Recall tells us how many Positive cases were found.
Recall is important when missing a Positive case is dangerous.
Recall alone is not enough; it should be used with Precision.
------------


## Question 
Basics
What is Recall?
Why do we use Recall?
What does Recall measure?
Write the Recall formula?
What is True Positive (TP)?
What is False Negative (FN)?
What is the range of Recall?
Can Recall be greater than 100%?
Can Recall be negative?
Is Recall an Evaluation Metric?
Explain why High Recall does not always mean a good model.
Give one real-life example where Recall is more important than Precision.
Why should Precision and Recall be used together?

## Conceptual Questions

What is the meaning of High Recall?
What is the meaning of Low Recall?
Why is Recall important?
Which errors does Recall try to reduce?
Why is Recall important in Disease Detection?
Why is Recall important in Cancer Detection?
Why is Recall important in Fraud Detection?
Can a model have 100% Recall and still be bad?Why?
What is the biggest limitation of Recall?


## Python Questions
Which function calculates Recall?
Which library provides recall_score()?
What are y_true and y_pred?
What does recall_score() return?
How do you convert Recall into percentage?
Does recall_score() internally calculate TP and FN?
What happens if there are no Actual Positive cases?
Can recall_score() work for multiclass classification?
Why should y_true and y_pred have the same length?
Explain the complete Recall workflow in Python.


## Comparison Questions

What is the difference between Precision and Recall?
Which metric focuses on Actual Positive cases?
Which metric focuses on Predicted Positive cases?
Which metric tries to reduce False Negatives?
Which metric tries to reduce False Positives?
Can Recall be high while Precision is low?
Give an example. Why do we need F1 Score?


## Fill in the Blanks

Recall uses __ and __.
TP stands for __.
FN stands for __.
Recall measures the ability to find __ cases.
High Recall means fewer __.
recall_score() belongs to __.
Recall is usually written as a __.
Recall focuses on __ Positive cases.
Recall is very useful in __ Detection.
Recall is always between __ and __.

	
## True / False

Recall is an Evaluation Metric. ( )
Recall uses TP and FN. ( )
High Recall means fewer False Negatives. ( )
Recall measures all predictions. ( )
Recall is important in Cancer Detection. ( )
Recall alone is enough to evaluate every model. ( )
recall_score() is available in Scikit-learn. ( )
Recall can never exceed 100%. ( )
High Recall always means the model is perfect. ( )
Precision and Recall are usually used together. ( )
```