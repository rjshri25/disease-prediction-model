import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_disease_prediction_model(data_path):
    try:
        # Load the data
        df = pd.read_csv(data_path)

        # Select features and target
        X = df[['Temp', 'preci', 'LAI', 'cases']]
        y = df['disease_risk']  # Assuming the target variable is named 'disease_risk'

        # Split the data into training and test sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        print(f'Model Accuracy: {accuracy:.2f}')

        # Save the model
        joblib.dump(model, 'models/disease_predictor.pkl')
        print('Model saved to models/disease_predictor.pkl')

    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == '__main__':
    data_path = 'path/to/maharashtra_disease_data.csv'  # Replace with actual data path
    train_disease_prediction_model(data_path)