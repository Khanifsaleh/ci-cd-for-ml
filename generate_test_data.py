# generate_test_data.py
import pandas as pd
from sklearn.datasets import make_classification

# Generate synthetic test dataset
X_test, y_test = make_classification(
    n_samples=200,   # Number of samples for test data
    n_features=5,    # Number of features
    n_classes=2,     # Number of classes
    random_state=42
)

# Create a DataFrame for test data
columns = [f'feature_{i}' for i in range(X_test.shape[1])]
test_data = pd.DataFrame(X_test, columns=columns)
test_data['target'] = y_test

# Save generated test data to a CSV file
test_data.to_csv('test_data.csv', index=False)