import os
import pandas as pd
import numpy as np
import time

from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score,mean_absolute_percentage_error
import pickle


def finetune_model(data,train_data,test_data):

    os.chdir("C:/Users/KISHORE/OneDrive/Desktop/Intelligent Weather Prediction Pipeline/models")
                
    for target in data.loc[:,"Temperature":"is_day"].columns:

        X_train = train_data.drop(columns=[target])
        y_train = train_data[target]

        X_test = test_data.drop(columns=[target])
        y_test = test_data[target]

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        param_dist = {
            'n_estimators': [100, 200, 300, 500, 800],
            'learning_rate': [0.01, 0.03, 0.05, 0.1, 0.2],
            'max_depth': [3, 4, 5, 6, 8, 10],
            'min_child_weight': [1, 3, 5, 7],
            'subsample': [0.6, 0.8, 1.0],
            'colsample_bytree': [0.6, 0.8, 1.0],
            'gamma': [0, 0.1, 0.3, 0.5],
            'reg_alpha': [0, 0.01, 0.1, 1],
            'reg_lambda': [1, 2, 5, 10]
        }

        filename = f"{target}_xgb_model.pkl"

        with open(filename,"rb") as file:
            loaded_model = pickle.load(file)


        
        rm_search = RandomizedSearchCV(
            estimator=loaded_model,
            param_distributions=param_dist,
            n_iter=50,
            scoring='neg_root_mean_squared_error',
            cv=5,
            verbose=2,
            random_state=42,
            n_jobs=-1
        )

        rm_search.fit(X_train_scaled,y_train)

        best_model = rm_search.best_estimator_

        filename = f"fine_{target}_xgb_model.pkl"

        with open(filename,"wb") as file:
            pickle.dump(best_model,file)

    return 0

def tune_rf_model(model,params,cv,X_train,y_train,X_test,y_test):

    search = RandomizedSearchCV(
        estimator=model,
        param_distributions=params,
        n_iter=30,
        scoring="neg_root_mean_squared_error",
        cv=cv,
        random_state=42,
        n_jobs=-1,
        verbose=1
    )

    start = time.time()

    search.fit(X_train, y_train)
    cv_results = pd.DataFrame(search.cv_results_)

    model_train_time = time.time() - start

    best_model = search.best_estimator_

    start = time.time()

    model_pred = best_model.predict(X_test)

    model_inference_time = time.time() - start

    mae = mean_absolute_error(y_test, model_pred)
    rmse = np.sqrt(mean_squared_error(y_test, model_pred))
    r2 = r2_score(y_test, model_pred)
    mape = mean_absolute_percentage_error(y_test, model_pred) * 100

    return mae,rmse,r2,mape,model_train_time,model_inference_time,cv_results,model_pred,best_model

def tune_lgbm_model(model,params,cv,X_train,y_train,X_test,y_test):

    search = RandomizedSearchCV(
        estimator=model,
        param_distributions=params,
        n_iter=30,
        scoring="neg_root_mean_squared_error",
        cv=cv,
        random_state=42,
        n_jobs=-1,
        verbose=1
    )

    start = time.time()

    search.fit(X_train, y_train)

    cv_results = pd.DataFrame(search.cv_results_)

    model_train_time = time.time() - start

    best_model = search.best_estimator_

    start = time.time()

    model_pred = best_model.predict(X_test)

    model_inference_time = time.time() - start

    mae = mean_absolute_error(y_test, model_pred)
    rmse = np.sqrt(mean_squared_error(y_test, model_pred))
    r2 = r2_score(y_test, model_pred)
    mape = mean_absolute_percentage_error(y_test, model_pred) * 100


    return mae,rmse,r2,mape,model_train_time,model_inference_time,cv_results,model_pred,best_model

