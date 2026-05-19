import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_preprocess():
    
    df = pd.read_csv("data/raw/house_data.csv")

    encoder = LabelEncoder()
    df["location"] = encoder.fit_transform(df["location"])

    X = df[["area", "bedrooms", "location"]]
    y = df["price"]

    return X, y