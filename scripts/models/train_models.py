import os
import pandas as pd
import numpy as np

from scripts.models import fine_tune_models

from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from lightgbm import LGBMRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
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

def random_forest(X_train,y_train,X_test,y_test):
    cv = KFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    rf_model = RandomForestRegressor(random_state=42)
    rf_params = {
        "n_estimators": [100, 200, 300, 500],
        "max_depth": [10, 20, 30, None],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [1, 2, 4],
        "max_features": ["sqrt", "log2", None]
    }

    rf_mae,rf_rmse,rf_r2,rf_mape,rf_model_train_time,rf_model_inference_time,cv_results,model_pred,rf_best_model = fine_tune_models.tune_rf_model(rf_model,rf_params,cv,X_train,y_train,X_test,y_test)

    return rf_mae,rf_rmse,rf_r2,rf_mape,rf_model_train_time,rf_model_inference_time,cv_results,model_pred,rf_best_model


def lgbm_model(X_train,y_train,X_test,y_test):
    cv = KFold(
        n_splits=5,
        shuffle=True,
        random_state=42
    )

    lgbm = LGBMRegressor(
        objective="regression",
        random_state=42
    )
    lgbm_params = {
        "n_estimators": [100, 200, 300, 500],
        "learning_rate": [0.01, 0.03, 0.05, 0.1],
        "max_depth": [-1, 5, 10, 15],
        "num_leaves": [31, 50, 80, 120],
        "subsample": [0.7, 0.8, 1.0],
        "colsample_bytree": [0.7, 0.8, 1.0],
        "min_child_samples": [10, 20, 30]
    }

    xgbm_mae,xgbm_rmse,xgbm_r2,xgbm_mape,xgbm_model_train_time,xgbm_model_inference_time,cv_results,model_pred,xgbm_best_model = fine_tune_models.tune_lgbm_model(lgbm,lgbm_params,cv,X_train,y_train,X_test,y_test)

    return xgbm_mae,xgbm_rmse,xgbm_r2,xgbm_mape,xgbm_model_train_time,xgbm_model_inference_time,cv_results,model_pred,xgbm_best_model



