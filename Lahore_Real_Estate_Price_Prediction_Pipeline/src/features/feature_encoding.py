import pandas as pd
from sklearn.model_selection import train_test_split
from category_encoders import TargetEncoder
from sklearn.preprocessing import OneHotEncoder

def encode_features(data):
    """
    Collects Weather data of Delhi for weather forcasting pipeline

    Args:
        data (DataFrame): it contains Lahore House Listings from Zameen.com (2025).

    Returns:
        X_train (DataFrame):Contains training data with encoded features.
        X_test (DataFrame):Contains test data with encoded features.
        y_train (DataFrame):Contains train price data 
        y_test (DataFrame):Contains training price data 
        target_encoder, encoder (Encoders): Target and onehot encoders.
    
    """

    bool_cols = data.select_dtypes(include="bool").columns
    data[bool_cols] = data[bool_cols].astype(int)

    train = data.drop(columns=["Price_PKR"])
    test = data["Price_PKR"]

    X_train, X_test, y_train, y_test = train_test_split(train,test,test_size=0.2,random_state=42)

    target_encoder = TargetEncoder(cols=["Location_Normalized"])
    X_train["Location_Normalized"] = target_encoder.fit_transform(X_train["Location_Normalized"],y_train)
    X_test["Location_Normalized"] = target_encoder.transform(X_test["Location_Normalized"])

    categorical_cols = ["Type", "Purpose"]
    encoder = OneHotEncoder(sparse_output=False,handle_unknown="ignore")
    train_encoded = encoder.fit_transform(X_train[categorical_cols])
    test_encoded = encoder.transform(X_test[categorical_cols])

    train_encoded = pd.DataFrame(train_encoded,columns=encoder.get_feature_names_out(categorical_cols),index=X_train.index)
    test_encoded = pd.DataFrame(test_encoded,columns=encoder.get_feature_names_out(categorical_cols),index=X_test.index)

    X_train = pd.concat([X_train, train_encoded], axis=1)
    X_test = pd.concat([X_test, test_encoded], axis=1)

    return X_train, X_test, y_train, y_test, target_encoder, encoder