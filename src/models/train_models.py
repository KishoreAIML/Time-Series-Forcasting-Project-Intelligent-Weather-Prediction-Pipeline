from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import pandas as pd


class ml_models:

    def __init__(self,data,train_data,test_data):
        self.data = data
        self.train_data = train_data
        self.test_data = test_data
    def xgbmodel(self):
        results = []

        for target in self.data.columns:
            X_train = self.train_data.drop(columns=[target])
            y_train = self.train_data[target]

            X_test = self.test_data.drop(columns=[target])
            y_test = self.test_data[target]

            model = XGBRegressor(
                n_estimators=300,
                learning_rate=0.05,
                max_depth=6,
                random_state=42
            )

            model.fit(X_train, y_train)

            pred = model.predict(X_test)

            mae = mean_absolute_error(y_test, pred)
            rmse = np.sqrt(mean_squared_error(y_test, pred))
            r2 = r2_score(y_test, pred)

            results.append([target, mae, rmse, r2])

        evaluation = pd.DataFrame(
            results,
            columns=["Target", "MAE", "RMSE", "R²"]
            )
        return evaluation,model