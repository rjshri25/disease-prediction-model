# train.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the dataset
data = pd.read_csv('maharashtra_disease_data.csv')

# Feature Engineering
# Assuming the data has columns: 'temperature', 'precipitation', 'LAI', 'cases', 'deaths'
data['temp_precipitation'] = data['temperature'] * data['precipitation']
data['temp_LAI'] = data['temperature'] * data['LAI']
data['precipitation_LAI'] = data['precipitation'] * data['LAI']

# Define features and target
features = ['temperature', 'precipitation', 'LAI', 'cases', 'deaths', 
            'temp_precipitation', 'temp_LAI', 'precipitation_LAI']
target = 'disease_outcome'  # Assuming the target column is named 'disease_outcome'

X = data[features]
y = data[target]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Save the model
joblib.dump(model, 'random_forest_model.joblib')
