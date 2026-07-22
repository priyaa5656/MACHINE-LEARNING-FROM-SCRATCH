from sklearn.metrics import precision_score

# Actual Values

y_true = [
    1,
    0,
    1,
    1,
    0,
    1,
    0,
    1
]

# Predicted Values

y_pred = [
    1,
    0,
    1,
    0,
    0,
    1,
    1,
    1
]

# Calculate Precision

precision = precision_score(y_true, y_pred)

print("Precision :", precision)

print("Precision Percentage :", precision * 100)


## Output:  Precision : 0.8
##Precision Percentage : 80.0