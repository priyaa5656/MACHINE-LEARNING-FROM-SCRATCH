from sklearn.metrics import accuracy_score

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
    0,
    1
]

# Accuracy

accuracy = accuracy_score(y_true, y_pred)

print("Accuracy :", accuracy)

print("Accuracy Percentage :", accuracy * 100)





## output: 
#Accuracy : 0.875
#Accuracy Percentage : 87.5