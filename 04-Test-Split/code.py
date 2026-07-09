# ==========================================
# Train/Test Split Example
# ==========================================

# Import Required Libraries
import numpy as np
from sklearn.model_selection import train_test_split

# ==========================================
# Step 1 : Create Input Data (Features)
# Study Hours
# ==========================================

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8]
])

# ==========================================
# Step 2 : Create Output Data (Labels)
# Student Marks
# ==========================================

y = np.array([
    40,
    50,
    60,
    70,
    80,
    90,
    95,
    98
])

# ==========================================
# Step 3 : Split the Dataset
# 80% Training
# 20% Testing
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================================
# Step 4 : Print Original Dataset
# ==========================================

print("=" * 40)
print("Original Features (X)")
print(X)

print("\nOriginal Labels (y)")
print(y)

# ==========================================
# Step 5 : Print Training Data
# ==========================================

print("\n" + "=" * 40)
print("Training Features (X_train)")
print(X_train)

print("\nTraining Labels (y_train)")
print(y_train)

# ==========================================
# Step 6 : Print Testing Data
# ==========================================

print("\n" + "=" * 40)
print("Testing Features (X_test)")
print(X_test)

print("\nTesting Labels (y_test)")
print(y_test)

# ==========================================
# Step 7 : Number of Rows
# ==========================================

print("\n" + "=" * 40)
print("Total Rows       :", len(X))
print("Training Rows    :", len(X_train))
print("Testing Rows     :", len(X_test))

# ==========================================
# Step 8 : Change test_size
# Uncomment to test
# ==========================================

"""
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTesting Rows after test_size=0.3")
print(len(X_test))
"""

# ==========================================
# Step 9 : Change random_state
# Uncomment to test
# ==========================================

"""
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=10
)

print("\nTraining Features")
print(X_train)

print("\nTesting Features")
print(X_test)
"""

# ==========================================
# Step 10 : Remove random_state
# Run this block multiple times
# Observe the output
# ==========================================

"""
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2
)

print("\nTraining Features")
print(X_train)

print("\nTesting Features")
print(X_test)
"""

# ==========================================
# End of Program
# ==========================================