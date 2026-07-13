# What is Feature Scaling?

Feature Scaling is a technique used to make all input features have a similar range before training a Machine Learning model.

In simple words: Feature Scaling means **bringing different values to a similar scale** so that the Machine Learning model can learn fairly from all features.

---

## 🤔 Why Do We Need Feature Scaling?

Imagine you have two students.

Student A
Height = 170 cm

Student B
Salary = ₹50,00,000

Can we compare these numbers directly?

```text
170

vs

5000000
```

No. The salary value is much larger than the height value. If we give these values directly to a Machine Learning model, the model will pay much more attention to Salary and almost ignore Height. This can lead to poor learning. 

So we first scale both values to a similar range.


---
##  Real-Life Example 1

Imagine a race. Runner A starts at 0 meters. Runner B starts at 1000 meters.

Can you compare who is faster?

❌ No.Both runners should start from the same position.

Feature Scaling does the same thing.
It brings every feature to a similar scale before learning starts.


---
## Example 2

Suppose you want to predict the price of a house. Your dataset looks like this.

| Area (sqft) | Age (Years) |
|-------------|-------------|
|1000         |5|
|1500         |8|
|2000         |10|

Notice the values.

```text
| Area (sqft) | 
|-------------|
|1000         |
|1500         |
|2000         |

|Age|
|---|
|5  |
|8  |
|10 |
```

Area has much bigger numbers. Age has much smaller numbers.

Without Feature Scaling, the Machine Learning model may think Area is much more important, only because its numbers are larger.

This is not correct.

---

## Another Example

Suppose a dataset contains:

Age

```text
18
25
30
40
```

Salary

```text
30000
50000
80000
150000
```

Clearly, Salary values are much bigger. The model may focus mostly on Salary.

Feature Scaling makes both features comparable.

---
## Why is Feature Scaling Important?

Feature Scaling helps the Machine Learning model

- Learn faster.
- Reduce training time.
- Improve accuracy.
- Prevent one feature from dominating others.
- Help Gradient Descent converge faster.


---
## Which Algorithms Need Feature Scaling?

Feature Scaling is important for:

✅ Linear Regression (Gradient Descent)  
✅ Logistic Regression  
✅ KNN  
✅ SVM  
✅ K-Means Clustering  
✅ Neural Networks


---

Feature Scaling is usually **not required** for:

✅ Decision Tree  
✅ Random Forest  
✅ XGBoost

Because these algorithms split data based on conditions, not on distances.


---

---

## Easy Trick to Remember

```text
Different Scales

↓

Model Gets Confused

↓

Feature Scaling

↓

Similar Scales

↓

Better Learning

↓

Better Prediction
```

---
## Easy word:

Feature Scaling is the process of converting features into a similar range so that every feature contributes fairly during model training.

---
## Summary

✅ Used before training the model.  
✅ Makes all features similar in scale.  
✅ Prevents large values from dominating.  
✅ Helps Gradient Descent learn faster.  
✅ Improves model performance.


## Types of Feature Scaling

Feature Scaling can be done using different techniques. The two most common Feature Scaling techniques are:

1. Normalization (Min-Max Scaling)      
2. Standardization (Z-Score Scaling)

Both techniques reduce the difference between large and small values, but they do it in different ways.






---
## 1. Normalization (Min-Max Scaling)

Normalization converts all values into a fixed range, usually between **0 and 1**. It uses the **Minimum** and **Maximum** values of the dataset.

In simple words: Normalization changes large and small numbers into a similar range without changing their order.

---

## 🤔 Why Do We Need Normalization?

Imagine two features.

| Age | Salary |
|------|---------|
|20|20000|
|30|50000|
|40|100000|

Notice the values.

```text
Age

20
30
40

Salary

20000
50000
100000
```

Salary values are much larger. The Machine Learning model may think Salary is more important.  
Normalization brings both features into the same range.



---

## Formula
Normalization uses the following formula.

```text
Normalized Value = (Value − Minimum Value) / (Maximum Value − Minimum Value)
```
Or simply,

```text
x'=  (x −min) / (max − min)

where

x = Original Value

min = Smallest Value

max = Largest Value

x' = Normalized Value
```


---
## Step-by-Step Example
Dataset

```text
10  
20  
30  
40  
50
```

```
Minimum = 10

Maximum = 50
```

Now normalize  is 

```text
- First value= 10

(10−10)/(50−10) = 0/40 = 0


- Second value= 20

(20−10)/(50−10) = 10/40 = 0.25


- Third value =30

(30−10)/(50−10) = 20/40 = 0.50


- Fourth value= 40

(40−10)/(50−10) = 30/40 = 0.75


- Fifth value=50

(50−10)/(50−10) = 40/40 = 1.00


Final Dataset =

```text
Original

10

20

30

40

50


↓

Normalized


0.00

0.25

0.50

0.75

1.00
```

---

## 🌍 Real-Life Example

Imagine three students.

Student A

Height = 150 cm

Student B

Height = 170 cm

Student C

Height = 190 cm

Instead of using actual heights, Normalization converts them to

```text
150 → 0.0

170 → 0.5

190 → 1.0
```

The order remains the same. Only the scale changes.

## Important Properties
```
Minimum Value
↓
Always becomes 0


Maximum Value
↓
Always becomes 1


Every other value lies between 0 and 1
```

---
## Advantages
✅ Easy to understand  
✅ Speeds up learning  
✅ Helps Gradient Descent  
✅ Useful when features have different scales

---
## Disadvantages
❌ Sensitive to Outliers 
If one value is extremely large, all other values become compressed.


---
## When Should We Use Normalization?
Normalization is commonly used in

✅ KNN  
✅ Neural Networks  
✅ Gradient Descent  
✅ Distance-based Algorithms

---

## Easy Trick

```text
Large Numbers

↓

Min-Max Formula

↓

0 to 1

↓

Better Learning
```


---
## In easy word

Normalization is a Feature Scaling technique that converts values into the range of **0 to 1** using the Min-Max formula.

---

## Summary
✅ Range becomes 0 to 1.   
✅ Smallest value becomes 0.   
✅ Largest value becomes 1.   
✅ Order of data remains the same.  
✅ Improves model performance.



---
## 2. Standardization (Z-Score Scaling)
Standardization is a Feature Scaling technique that transforms the data so that it has a **Mean (Average) of 0** and a **Standard Deviation of 1**.
Standardization converts the data so that:

It uses the **Mean** and **Standard Deviation** of the dataset.

In simple words: Standardization changes large and small numbers into a similar scale by measuring how far each value is from the average.

## 🤔 Why Do We Need Standardization?

Imagine two features.

| Age | Salary |
|------|---------|
|20|20000|
|30|50000|
|40|100000|

Notice the values.

```text
Age

20
30
40

Salary

20000
50000
100000
```

Salary values are much larger. The Machine Learning model may give more importance to Salary.

Standardization brings both features to a similar scale.

Unlike Normalization, the values are **not limited between 0 and 1**.

---

## Formula
Standardization uses the following formula.

```text
Standardized Value = (Value − Mean) / Standard Deviation

Or simply,   
z = (x − μ) / σ

where

x = Original Value

μ = Mean (Average)

σ = Standard Deviation

z = Standardized Value
```

---
## Step-by-Step Example

Dataset

```text
10
20
30
40
50
```

```
Mean = 30

Standard Deviation ≈ 14.14
```

Now standardize

```text
-First value = 10    
z1 = (10−30)/14.14    
z1 ≈ -1.41


- Second value = 20       
z2= (20−30)/14.14    
z2 ≈ -0.71


- Third value = 30    
z3= (30−30)/14.14    
z3= 0


- Fourth value = 40    
z4= (40−30)/14.14    
z4 ≈ 0.71


- Fifth value = 50     
z5= (50−30)/14.14    
z5 ≈ 1.41
```

Final Dataset

```text
Original

10

20

30

40

50


↓

Standardized


-1.41

-0.71

0.00

0.71

1.41
```



---
## 🌍 Real-Life Example
Imagine a class of students.

Average Marks = 70

Student A = 50 Marks

Student B = 70 Marks

Student C = 90 Marks

After Standardization,

```text
50 → -1.41

70 → 0

90 → 1.41
```

Students below the average get negative values.

Students equal to the average become 0.

Students above the average get positive values.



---
## Important Properties
```text
Mean
↓
Always becomes 0


Standard Deviation
↓
Always becomes 1


Values can be Negative / Zero / Positive
```


---
## Advantages
✅ Works well even when data has large values            
✅ Less affected by Outliers    
✅ Helps Gradient Descent   
✅ Widely used in Machine Learning

---

## Disadvantages  
❌ Values are not limited between 0 and 1    
❌ Slightly harder to understand than Normalization


---
## When Should We Use Standardization?
Standardization is commonly used in     
✅ Linear Regression    
✅ Logistic Regression   
✅ Support Vector Machine (SVM)   
✅ Principal Component Analysis (PCA)   
✅ Neural Networks



---
## Easy Trick

```text
Original Data

↓

Subtract Mean

↓

Divide by Standard Deviation

↓

Mean = 0

↓

Standard Deviation = 1
```


---
## In easy word
Standardization is a Feature Scaling technique that converts data so that its **Mean becomes 0** and its **Standard Deviation becomes 1**.


---
## Summary
✅ Mean becomes 0.    
✅ Standard Deviation becomes 1.   
✅ Values can be negative, zero, or positive.  
✅ Less sensitive to Outliers than Normalization.  
✅ Improves model performance.



---
## Easy Comparison
|       Normalization         |           Standardization        |
|---------------------------- |----------------------------------|
| Range becomes 0 to 1        | No fixed range                   |
| Uses Minimum and Maximum    | Uses Mean and Standard Deviation |
| Sensitive to Outliers       | Less sensitive to Outliers       |
| Also called Min-Max Scaling | Also called Z-Score Scaling      |


---
## Easy Trick
```text
Feature Scaling
        ├──────────────|
Normalization     Standardization
        │              │

     0 to 1      Mean = 0

                  Std = 1
```



---
## Difference Between Normalization and Standardization
Normalization and Standardization are both Feature Scaling techniques. Both are used to bring data to a similar scale. However, they work in different ways.

## Main Difference
Normalization says:   
> "Bring everything between 0 and 1."

Standardization says:    
> "Move everything around the average (Mean = 0)."

---
## Easy Example
Suppose we have the following dataset.

```text
10
20
30
40
50
```

### After Normalization
```text
0.00

0.25

0.50

0.75

1.00
```
Notice, All values are now between **0 and 1**.

### After Standardization
```text
-1.41

-0.71

0.00

0.71

1.41
```
Notice, The values are **not between 0 and 1**. Some are negative,some are positive, and the average becomes **0**.


---
# Comparison Table
| Feature                  | Normalization        | Standardization                             |
|--------------------------|----------------------|-------------------------------------------- | 
| Also Called              | Min-Max Scaling      | Z-Score Scaling                             |
| Formula                  | (x-min)/(max-min)    | (x-μ)/σ                                     |
| Uses                     | Minimum & Maximum    | Mean & Standard Deviation                   |
| Range                    | 0 to 1               | No Fixed Range                              |
| Mean becomes             | No                   | Yes (0)                                     |
|Standard Deviation becomes| No                   | Yes (1)                                     |
| Negative Values          | No                   | Yes                                         |
| Sensitive to Outliers    | Yes                  | Less                                        |
| Easy to Understand       | Yes                  | Slightly Hard                               |
| Commonly Used In         | KNN, Neural Networks | Linear Regression, Logistic Regression, SVM |



---

# Which One is Better?  When Should We Use Which?
There is **no best method**. The choice depends on the Machine Learning algorithm and the data.          
Some algorithms work better with Normalization. Some algorithms work better with Standardization.Standardization is less affected by Outliers.


---
## Use Normalization When
Normalization is a good choice when the algorithm depends on the **distance between data points**.     
These algorithms work better when all features have values between **0 and 1**.   

Examples:     
✅ K-Nearest Neighbors (KNN)     
✅ Neural Networks     
✅ Gradient Descent    
✅ K-Means Clustering


---
## Use Standardization When
Standardization is a good choice when the data follows a **Normal (Gaussian) Distribution** or when the algorithm assumes data is centered around the mean.These algorithms usually perform better when Mean = 0 , Standard Deviation = 1

Examples:    
✅ Linear Regression    
✅ Logistic Regression    
✅ Support Vector Machine (SVM)    
✅ Principal Component Analysis (PCA)


---
## If You Don't Know Which One to Use
A simple rule is:

```text
Distance Based Algorithm
↓
Normalization
```

```text
Linear Model
↓
Standardization
```


---
## Summary
✅ Normalization → KNN, Neural Networks, K-Means       
✅ Standardization → Linear Regression, Logistic Regression, SVM, PCA

Always choose the scaling technique based on the algorithm and the dataset.


---
## ⚙️ Installation (Scikit-learn)
Feature Scaling is usually performed using the **Scikit-learn** library.


---
## Install Scikit-learn
```bash
pip install scikit-learn
```

---
## Check Installation
```python
import sklearn           
print(sklearn.__version__)
```
If no error appears, Scikit-learn has been installed successfully.


---
## Import Libraries
For Normalization
```python
from sklearn.preprocessing import MinMaxScaler
```

For Standardization
```python
from sklearn.preprocessing import StandardScaler
```


---
# 🛠️ Basic Syntax
Scikit-learn provides ready-made scaler objects.

---
## Normalization Syntax
```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(data)
```

---

## Standardization Syntax

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)
```

---

## Explain: 
```python
scaler = MinMaxScaler()
```

Creates a Normalization object.


---
```python
scaler = StandardScaler()
```

Creates a Standardization object.


---
```python
fit_transform(data)
```

This method performs two tasks together.


```text
fit()

↓

Learns information from the dataset.


For Normalization

↓

Finds Minimum and Maximum


For Standardization

↓

Finds Mean and Standard Deviation


↓

transform()

↓

Uses that information to scale the data.
```

---
## Easy Trick
```text
fit()
↓
Learn


transform()
↓
Apply


fit_transform()
↓
Learn + Apply
```

---
## Summary
✅ MinMaxScaler() → Normalization     
✅ StandardScaler() → Standardization     
✅ fit() learns from data.    
✅ transform() scales the data.    
✅ fit_transform() does both together.

---
Example: 




---
## Question : Complete the table.
| Algorithm          | Scaling Technique |
|--------------------|-------------------|
| KNN                |     N             |
| Linear Regression  |     S             |
| Logistic Regression|     S             |
| Neural Networks    |     N             |
| PCA                |     S             |
| K-Means            |     N             |
| SVM                |     S             |

---


---
## Questions

## Feature Scaling

1. What is Feature Scaling?
2. Why do we need Feature Scaling?
3. What problem occurs without Feature Scaling?
4. How does Feature Scaling help Gradient Descent?
5. Which Machine Learning algorithms require Feature Scaling?
6. Which algorithms usually do not require Feature Scaling?
7. Give one real-life example of Feature Scaling.
8. Is Feature Scaling done before or after model training?

---

## Normalization

9. What is Normalization?
10. Why do we use Normalization?
11. What is the range of Normalization?
12. Write the Min-Max Scaling formula.
13. What happens to the minimum value after Normalization?
14. What happens to the maximum value after Normalization?
15. Does Normalization change the order of the data?
16. What is one advantage of Normalization?
17. What is one disadvantage of Normalization?
18. Which Machine Learning algorithms commonly use Normalization?

---

## Standardization

19. What is Standardization?
20. Why do we need Standardization?
21. Write the Standardization formula.
22. What does `x` represent in the Standardization formula?
23. What does `μ (Mean)` represent?
24. What does `σ (Standard Deviation)` represent?
25. What is the range of Standardized data?
26. Can Standardized values be negative?
27. What happens to the Mean after Standardization?
28. What happens to the Standard Deviation after Standardization?
29. Does Standardization change the order of the data?
30. What is one advantage of Standardization?
31. What is one disadvantage of Standardization?
32. Which Machine Learning algorithms commonly use Standardization?
33. Can Standardization improve Gradient Descent?
34. What is the goal of Standardization?

---

## Comparison

35. What is the difference between Normalization and Standardization?
36. Which technique converts data into the range of 0 to 1?
37. Which technique makes the Mean equal to 0?
38. Which technique uses Minimum and Maximum values?
39. Which technique uses Mean and Standard Deviation?
40. Which technique is more sensitive to Outliers?
41. Which technique is also called Min-Max Scaling?
42. Which technique is also called Z-Score Scaling?

---

## Choosing the Right Technique

43. When should we use Normalization?
44. When should we use Standardization?
45. Which scaling technique is commonly used with KNN?
46. Which scaling technique is commonly used with Linear Regression?
47. Which scaling technique is commonly used with SVM?

---

## Python (Scikit-learn)

48. Which library is used for Feature Scaling?
49. How do you install Scikit-learn?
50. Which class is used for Normalization?
51. Which class is used for Standardization?
52. What is MinMaxScaler()?
53. What is StandardScaler()?
54. What does `fit()` do?
55. What does `transform()` do?
56. What does `fit_transform()` do?
57. Which method performs learning and scaling together?
58. Why do we use preprocessing classes in Scikit-learn?

---

## Practical Questions

59. Write the formulas of:
- Normalization
- Standardization

60. Which algorithm commonly uses **Normalization**?
- Linear Regression
- KNN
- Decision Tree

61. Which algorithm commonly uses **Standardization**?
- SVM
- Decision Tree
- Random Forest

62. Fill in the blanks.

| Question | Answer |
|----------|--------|
| Mean becomes ______ after Standardization. | |
| Standard Deviation becomes ______ after Standardization. | |
| Smallest value becomes ______ after Normalization. | |
| Largest value becomes ______ after Normalization. | |










