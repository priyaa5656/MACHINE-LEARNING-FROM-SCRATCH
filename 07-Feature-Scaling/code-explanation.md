## Code Explanation of Normalization 

## Step 1-  from sklearn.preprocessing import MinMaxScaler
Imports the **MinMaxScaler** class from Scikit-learn.

We use it for **Normalization**.


---
## Step 2- import numpy as np
Imports the NumPy library. NumPy is used to create arrays.


---
## Step 3 - data = np.array([[10],[20],[30],[40],[50]])
Creates the dataset. Here,
```text
10
20
30
40
50
```
are the original values.


---
## Step 4- print(data)
Prints the original dataset.    
Output: [[10],[20],[30],[40],[50]]


---
## Step 5-  scaler = MinMaxScaler()
Creates a Normalization object. Nothing happens yet. The object is only created.


---
## Step 6- normalized_data = scaler.fit_transform(data)
This is the most important line. It performs two tasks.


### fit()
Learns from the dataset. It finds
```text
Minimum = 10

Maximum = 50
```

---
### transform()
Uses the formula
```text
(Value - Minimum) / (Maximum - Minimum)
```
and converts every value between 0 and 1


---
## Step 7- print(normalized_data)
Prints the normalized dataset.

Output: 

```text
[[0.00]
 [0.25]
 [0.50]
 [0.75]
 [1.00]]
```

---
## Complete Flow
```text
Original Data
↓
Create MinMaxScaler
↓
fit()
↓
Find Minimum & Maximum
↓
transform()
↓
Apply Min-Max Formula
↓
Normalized Data (0 to 1)
```


---
## Easy Trick
```text
MinMaxScaler()
↓
fit()
↓
Learn
↓
transform()
↓
Scale
↓
0 to 1
```


---
## Summary      
✅ Import MinMaxScaler.      
✅ Create the scaler object.      
✅ Use fit_transform().     
✅ Data is converted into the range of **0 to 1**.



# ==========================================
# Feature Scaling using Standardization
# ==========================================


## Step 1- from sklearn.preprocessing import StandardScaler
Imports the **StandardScaler** class from Scikit-learn. We use it for **Standardization (Z-Score Scaling).**

---
## Step 2- import numpy as np
Imports the NumPy library. NumPy is used to create arrays.


---
## Step 3- data = np.array([[10],[20],[30],[40],[50]])
Creates the dataset. Original values are
```text
10
20
30
40
50
```

---

## Step 4- print(data)
Prints the original dataset.      
Output: [[10],[20],[30],[40],[50]]

---
## Step 5- scaler = StandardScaler()
Creates a StandardScaler object. No scaling happens yet.


---
## Step 6- standardized_data = scaler.fit_transform(data)
This is the most important line. It performs two tasks.

### fit()-
Learns information from the dataset. It calculates

Mean = 30,   Standard Deviation ≈ 14.14


---
### transform()
Uses the formula: (Value − Mean)/ Standard Deviation

It converts every value into its standardized form.

After Standardization    
Mean = 0 , Standard Deviation = 1


---
## Step 7- print(standardized_data)
Prints the standardized dataset.

Output:

```text
[[-1.41]
 [-0.71]
 [ 0.00]
 [ 0.71]
 [ 1.41]]
```

---
## Complete Flow
```text
Original Data
↓
Create StandardScaler
↓
fit()
↓
Find Mean & Standard Deviation
↓
transform()
↓
Apply Z-Score Formula
↓
Standardized Data
```

---
## Easy Trick
```text
StandardScaler()
↓
fit()
↓
Learn Mean & Std
↓
transform()
↓
Scale Data
↓
Mean = 0,   Std = 1
```

---
## Summary
✅ Import StandardScaler.       
✅ Create the scaler object.      
✅ Use fit_transform().      
✅ Data becomes centered around the Mean.     
✅ Mean becomes 0.    
✅ Standard Deviation becomes 1.











