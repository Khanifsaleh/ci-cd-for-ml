# Example: model testing script (test.py)
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

# Load the trained model
model = joblib.load('trained_model.joblib')  # Replace with the trained model filename

# Load test data for evaluation
test_data = pd.read_csv('test_data.csv')  # Replace with your test dataset filename

# Prepare test data
X_test = test_data.drop('target', axis=1)  # Replace 'target' with your target column
y_test = test_data['target']

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
