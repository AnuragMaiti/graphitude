import pandas as pd

from pandas.api.types import is_string_dtype
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from django.core.files.storage import FileSystemStorage

from sklearn.metrics import accuracy_score
from graphapp.views.transform_data import transform
import pickle
from sklearn.model_selection import train_test_split


input_json = {"graphapp_form_file_name": "CarPrice.csv",
              "graphapp_form_model_name": "carpricemodel",
              "graphapp_form_target_column_name": "CarName",
              "graphapp_form_predictive_model_algorithm": "Logistic Regression",
              "selected_columns": ["enginelocation", "wheelbase", "price"]}

predict_json = {"feature_values": {"enginelocation": ["front"], "wheelbase": [95], "price": [16000]},
                "graphapp_form_model_name": "carpricemodel",
                "graphapp_form_file_name": "CarPrice.csv",
                }

classifiers = {
    'Logistic Regression': LogisticRegression(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'Random Forest': RandomForestClassifier(random_state=42),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'SVM': SVC(random_state=42),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB()
}


def transform(input_json):
    fs = FileSystemStorage()
    file_path = fs.path(input_json["graphapp_form_file_name"])
    data = pd.read_csv(file_path)

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


def create_model(input_json):
    X_train_scaled, X_test_scaled, y_train, y_test = transform(input_json)
    clf = classifiers[input_json["graphapp_form_predictive_model_algorithm"]]
    clf.fit(X_train_scaled, y_train)
    y_pred = clf.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)

    fs = FileSystemStorage()
    pklFile = f"{input_json["graphapp_form_model_name"]}.pkl"
    file_path = fs.path(f"modelpkl/{pklFile}")

    with fs.open(file_path, 'wb') as file:
        pickle.dump(clf, file)
    return pklFile

def predict(predict_json):
    print(predict_json)
    data_dict = predict_json["feature_values"]
    data = pd.DataFrame(data_dict)

    pklFile = f"{predict_json["graphapp_form_model_name"]}.pkl"
    fs = FileSystemStorage()
    file_path = fs.path(f"modelpkl/{pklFile}")
    with fs.open(file_path, 'rb') as file:
      model = pickle.load(file)
    
    label_encoder = LabelEncoder()
    categorical_features = list()

    file_path = fs.path(predict_json["graphapp_form_file_name"])
    og = pd.read_csv(file_path)

    for feature in data.columns:
        if is_string_dtype(data[feature]):
            categorical_features.append(feature)

    print(categorical_features)

    for feature in categorical_features:
        label_encoder.fit(og[feature])
        data[feature] = label_encoder.transform(data[feature])
        
    scaler = StandardScaler()
    data = scaler.fit_transform(data)

    return model.predict(data)