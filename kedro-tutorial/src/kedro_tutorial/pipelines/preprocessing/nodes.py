import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.drop(columns=['RowNumber', 'CustomerId', 'Surname'])
    le = LabelEncoder()
    data['Gender'] = le.fit_transform(data['Gender'])
    data = pd.get_dummies(data, columns=['Geography', 'Card Type'])
    return data
