from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from typing import Dict
import pandas as pd
import logging

def split_data(data: pd.DataFrame, test_size: float, random_state: int) -> Dict:
    X = data.drop(columns='Exited')
    y = data['Exited']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return dict(train=(X_train, y_train), test=(X_test, y_test))

def train_model(train: Dict, random_state: int) -> RandomForestClassifier:
    X_train, y_train = train['train']
    rf_clf = RandomForestClassifier(random_state=random_state)
    rf_clf.fit(X_train, y_train)
    return rf_clf

def evaluate_model(model: RandomForestClassifier, test: Dict) -> None:
    X_test, y_test = test['test']
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    confusion_mat = confusion_matrix(y_test, y_pred)
    class_report = classification_report(y_test, y_pred)
    log = logging.getLogger(__name__)
    log.info("Model Accuracy: %s", accuracy)
    log.info("Confusion Matrix: \n%s", confusion_mat)
    log.info("Classification Report: \n%s", class_report)
