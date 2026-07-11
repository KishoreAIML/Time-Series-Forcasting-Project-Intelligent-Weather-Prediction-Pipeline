import os
import pandas as pd
import numpy as np


def add_features(data):
    """
    It creates new features from existing features in dataset(Feature Engineering)

    Args:
        data(DataFrame): dataset,it contains delhi weather data.

    Returns:
        data(DataFrame): returns dataset with new features they give extra context to the model.
    """
    
    #for Rolling mean & std
    num_cols = data.select_dtypes(include = np.number).columns
    rolling_mean_columns = [f"Rolling Mean of {col}" for col in num_cols]
    rolling_std_columns = [f"Rolling std of {col}" for col in num_cols]

    data[rolling_mean_columns] = data[num_cols].rolling(window=24).mean()
    data[rolling_std_columns] = data[num_cols].rolling(window=24).std()

    #Date Encoding

    ''''data["hour"] = data["Date"].dt.hour
    data["hour_sin"] = np.sin(2 * np.pi * data["hour"] / 24)
    data["hour_cos"] = np.cos(2 * np.pi * data["hour"] / 24)'''

    data["Day_of-year"] = data["Date"].dt.dayofyear
    data["Sine_Day_of-year"] = np.sin(((2 * np.pi) * data["Day_of-year"]) / 365)
    data["Cose_Day_of-year"] = np.cos(((2 * np.pi) * data["Day_of-year"]) / 365)

    data["day_of_week"] = data["Date"].dt.dayofweek
    data["day_of_month"] = data["Date"].dt.day
    data["month"] = data["Date"].dt.month
    data["quarter"] = data["Date"].dt.quarter
    data["is_weekend"] = (data["Date"].dt.dayofweek >= 5).astype(int)


    return data
    
