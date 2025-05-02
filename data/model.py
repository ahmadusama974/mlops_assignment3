# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib

# Load the preprocessed data
data = pd.read_csv(r'C:\Users\Admin\Desktop\mlops-ass3\mlops_assignment3\data\processed_data.csv')

# Check the first few rows to understand the data structure
print(data.head())

# Select features (independent variables) and target (dependent variable)
features = data[['Humidity (%)', 'Wind Speed (km/h)', 'Weather Condition']]  # Example features
target = data['Temperature (°C)']  # Example target (Temperature)

# Handle categorical features like 'Weather Condition' by encoding them
features = pd.get_dummies(features, drop_first=True)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Standardizing the numerical features
scaler = StandardScaler()

# Fit the scaler on the training data and transform both train and test data
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Calculate the Mean Squared Error and R-squared score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Save the trained model
joblib.dump(model, 'weather_predictor_model.pkl')

# Optionally, save the scaler as well (if you plan to use it later for new data)
joblib.dump(scaler, 'scaler.pkl')
