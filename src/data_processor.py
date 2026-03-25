import pandas as pd


def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)


def clean_data(df):
    """Perform data cleaning."""
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Handle missing values
    df = df.fillna(method='ffill')  # Forward fill for simplicity
    
    return df


def preprocess_data(df):
    """Preprocess the data for modeling."""
    # Convert categorical columns to numerical if needed
    df = pd.get_dummies(df)
    
    return df


if __name__ == '__main__':
    # Example use
    data = load_data('path/to/your/data.csv')
    cleaned_data = clean_data(data)
    processed_data = preprocess_data(cleaned_data)
    print(processed_data.head())
