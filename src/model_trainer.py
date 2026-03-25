from sklearn.ensemble import RandomForestClassifier
import pandas as pd

class ModelTrainer:
    def __init__(self, n_estimators=100):
        self.model = RandomForestClassifier(n_estimators=n_estimators)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)

# Example usage:
# data = pd.read_csv('data.csv')
# X = data.drop('target', axis=1)
# y = data['target']
# trainer = ModelTrainer()
# trainer.train(X, y)
# predictions = trainer.predict(X)