import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load raw data
raw_data_path = r'C:\Users\Admin\Desktop\mlops-ass3\mlops_assignment3\data\raw_data.csv'
df = pd.read_csv(raw_data_path)

# Handle missing values
df.dropna(inplace=True)

# Select numerical columns to standardize
numerical_features = ['Temperature (°C)', 'Wind Speed (km/h)']

# Initialize scaler
scaler = StandardScaler()

# Apply standardization
df[numerical_features] = scaler.fit_transform(df[numerical_features])

# Save preprocessed data
processed_data_path = r'C:\Users\Admin\Desktop\mlops-ass3\mlops_assignment3\data\processed_data.csv'
df.to_csv(processed_data_path, index=False)

print("✅ Preprocessing complete. Processed data saved to data/processed_data.csv")
