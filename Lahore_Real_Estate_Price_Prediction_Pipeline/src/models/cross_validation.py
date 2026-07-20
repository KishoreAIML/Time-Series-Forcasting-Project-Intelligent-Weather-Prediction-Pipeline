from sklearn.model_selection import cross_validate


def cross_validate_rf(model,X_train,y_train,cv):
    cv = cross_validate(
        estimator=model,
        X=X_train,
        y=y_train,
        cv=cv,
        scoring={
            "MAE": "neg_mean_absolute_error",
            "RMSE": "neg_root_mean_squared_error",
            "R2": "r2",
            "MAPE": "neg_mean_absolute_percentage_error"
        },
        n_jobs=-1
    )

    cv_mae = -cv["test_MAE"].mean()
    cv_rmse = -cv["test_RMSE"].mean()
    cv_r2 = cv["test_R2"].mean()
    cv_mape = -cv["test_MAPE"].mean() * 100

    return cv_mae,cv_rmse,cv_r2,cv_mape