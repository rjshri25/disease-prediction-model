import pandas as pd
import numpy as np
from datetime import datetime

# Function to derive weather-based features

def weather_features(df):
    # Convert the date column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Derive Season feature
    df['season'] = df['date'].dt.month.map({
        1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring',
        5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer',
        9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Winter'
    })

    # Derive Rainfall Level feature
    df['rainfall_level'] = pd.cut(df['rainfall'], bins=[0, 5, 15, 30, np.inf], 
                                   labels=['Low', 'Moderate', 'High', 'Very High'])

    # Derive Temperature Level feature
    df['temperature_level'] = pd.cut(df['temperature'], bins=[-np.inf, 0, 15, 25, 35, np.inf], 
                                      labels=['Freezing', 'Cold', 'Moderate', 'Hot', 'Very Hot'])

    # Create interaction features
    df['rain_temp_interaction'] = df['rainfall'] * df['temperature']

    return df

# Example usage:
# df = pd.DataFrame({'date': [], 'rainfall': [], 'temperature': []})
# df_with_features = weather_features(df)
