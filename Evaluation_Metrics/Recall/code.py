from sklearn.metrics import recall_score

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

# Calculate Recall

recall = recall_score(y_true, y_pred)

print("Recall :", recall)

print("Recall Percentage :", recall * 100)