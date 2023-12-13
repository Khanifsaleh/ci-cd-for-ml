# preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load generated data
data = pd.read_csv('generated_data.csv')

# Perform data preprocessing tasks
scaler = StandardScaler()
numerical_cols = [col for col in data.columns if col.startswith('feature')]
data[numerical_cols] = scaler.fit_transform(data[numerical_cols])

# Save preprocessed data
data.to_csv('preprocessed_data.csv', index=False)
