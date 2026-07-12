import os
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np
import pickle


def xgbmodel(data,train_data,test_data):
    """
    To train XGBoost model a gradient boosting framework for regression.

    Args:
        1.data(DataFrame) : weather dataset i.e, processed dataset.
        2.train_data(DataFrame) : weather data without target features(Y) (90%)
        3.tesst_data(DataFrame) : weather data only with target feature (10%)
    
    Returns:
        evaluation(DataFrame) : contains evaluation metrics of the trained model.
    
    """
    results = []
    os.chdir("C:/Users/KISHORE/OneDrive/Desktop/Intelligent Weather Prediction Pipeline/models")

    for target in data.loc[:,"Temperature":"is_day"].columns:

        X_train = train_data.loc[:, train_data.columns != target]
        y_train = train_data.loc[:, target]

        input_features = X_train.columns

        X_test = test_data.drop(columns=[target])
        y_test = test_data[target]

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        model = XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            random_state=42
        )

        model.fit(X_train_scaled,y_train)

        pred = model.predict(X_test_scaled)

        mae = mean_absolute_error(y_test, pred)
        rmse = np.sqrt(mean_squared_error(y_test, pred))
        r2 = r2_score(y_test, pred)

        filename = f"{target}_xgb_model.pkl"
        results.append([target, mae, rmse, r2, filename])
        with open(filename,"wb") as file:
            pickle.dump(model,file)

        scaler_name = f"{target}_standard_scaler.pkl"
        with open(scaler_name, "wb") as f:
            pickle.dump(scaler, f)
            

    evaluation = pd.DataFrame(
        results,
        columns=["Target", "MAE", "RMSE", "R²", "Filename"]
    )
    return evaluation,input_features