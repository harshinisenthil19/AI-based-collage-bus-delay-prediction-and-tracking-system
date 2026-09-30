import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

# Load dataset
data = pd.read_csv("bus_data.csv")

# Convert text values into numbers
traffic_encoder = LabelEncoder()
weather_encoder = LabelEncoder()

data["traffic"] = traffic_encoder.fit_transform(data["traffic"])
data["weather"] = weather_encoder.fit_transform(data["weather"])

# Input features
X = data[
    ["distance", "traffic", "weather", "previous_delay"]
]

# Target value
y = data["actual_delay"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create ML model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

# Calculate error
error = mean_absolute_error(y_test, predictions)

print("AI Bus Delay Prediction Model")
print("-----------------------------")
print("Mean Absolute Error:", round(error, 2), "minutes")

# Example prediction
sample = [[12, 0, 1, 5]]

predicted_delay = model.predict(sample)

print(
    "Predicted Bus Delay:",
    round(predicted_delay[0], 2),
    "minutes"
)
