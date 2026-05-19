import os

from src.train import train_model

def test_model():

    model, X_test, y_test = train_model()

    assert model is not None

    assert os.path.exists("models/model.pkl")