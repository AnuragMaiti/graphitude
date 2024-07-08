import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pandas.api.types import is_string_dtype
from sklearn.preprocessing import LabelEncoder

def transform(input_json):
    filepath = f"experimental/{input_json["graphapp_form_file_name"]}"
    data = pd.read_csv(filepath)
    X = data[input_json["selected_columns"]]
    y = data[input_json["graphapp_form_target_column_name"]]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    categorical_features = list()
    numeric_features = list()
    label_encoder = LabelEncoder()

    for feature in X.columns:
        if is_string_dtype(X[feature]):
            categorical_features.append(feature)
        else:
            numeric_features.append(feature)

    for feature in categorical_features:
        X_train[feature] = label_encoder.fit_transform(X_train[feature])
        X_test[feature] = label_encoder.fit_transform(X_test[feature])

    scaler = StandardScaler()

    X_train_scaled = X_train.copy()  
    X_train_scaled = scaler.fit_transform(X_train)

    X_test_scaled = X_test.copy() 
    X_test_scaled = scaler.fit_transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test
