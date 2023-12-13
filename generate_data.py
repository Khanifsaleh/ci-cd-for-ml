# generate_data.py
from sklearn.datasets import make_classification
import pandas as pd

# Generate synthetic dataset
X, y = make_classification(
    n_samples=1000,  # Number of samples
    n_features=5,    # Number of features
    n_classes=2,     # Number of classes
    random_state=42
)

# Create a DataFrame from generated data
columns = [f'feature_{i}' for i in range(X.shape[1])]
data = pd.DataFrame(X, columns=columns)
data['target'] = y

# Save generated data to a CSV file
data.to_csv('generated_data.csv', index=False)
