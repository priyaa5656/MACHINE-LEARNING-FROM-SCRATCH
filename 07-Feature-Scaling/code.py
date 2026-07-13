# ==========================================
# Feature Scaling using Normalization
# ==========================================

# Import Library
from sklearn.preprocessing import MinMaxScaler

# Import NumPy
import numpy as np

# ------------------------------------------
# Step 1 : Create Dataset
# ------------------------------------------

data = np.array([
    [10],
    [20],
    [30],
    [40],
    [50]
])

print("Original Data")
print(data)

# ------------------------------------------
# Step 2 : Create MinMaxScaler Object
# ------------------------------------------

scaler = MinMaxScaler()

# ------------------------------------------
# Step 3 : Normalize the Data
# ------------------------------------------

normalized_data = scaler.fit_transform(data)

# ------------------------------------------
# Step 4 : Print Result
# ------------------------------------------

print("\nNormalized Data")
print(normalized_data)



# ==========================================
# Feature Scaling using Standardization
# ==========================================

# Import Library
from sklearn.preprocessing import StandardScaler

# Import NumPy
import numpy as np

# ------------------------------------------
# Step 1 : Create Dataset
# ------------------------------------------

data = np.array([
    [10],
    [20],
    [30],
    [40],
    [50]
])

print("Original Data")
print(data)

# ------------------------------------------
# Step 2 : Create StandardScaler Object
# ------------------------------------------

scaler = StandardScaler()

# ------------------------------------------
# Step 3 : Standardize the Data
# ------------------------------------------

standardized_data = scaler.fit_transform(data)

# ------------------------------------------
# Step 4 : Print Result
# ------------------------------------------

print("\nStandardized Data")
print(standardized_data)