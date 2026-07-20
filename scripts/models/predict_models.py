import pandas as pd
import numpy as np
import pickle
import os

os.chdir("C:/Users/KISHORE/OneDrive/Desktop/Intelligent Weather Prediction Pipeline/models")
def forcast(new_data,target):
    """
    Predict future target value with trained and fine tuned model.

    Args:
        1.new_data(numpyArray) : input features (X)
        2.target(String) : target feature name (Y)
    
    Returns:
        Predicted_data(Array) : contains predicted value
    
    """

    with open(f'fine_{target}_xgb_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)


    scaler_name = f"{target}_standard_scaler.pkl"
    with open(scaler_name, "rb") as f:
       scaler = pickle.load(f)

    new_data = np.array(new_data).reshape(1, -1)

    data_scaled = scaler.transform(new_data)

    Predicted_data = loaded_model.predict(data_scaled)

    return Predicted_data


