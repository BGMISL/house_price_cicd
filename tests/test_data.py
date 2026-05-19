from src.data_preprocessing import load_and_preprocess

def test_data():

    X, y = load_and_preprocess()

    assert X.shape[0] > 0
    assert y.shape[0] > 0