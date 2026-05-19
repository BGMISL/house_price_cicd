from sklearn.metrics import r2_score

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    score = r2_score(y_test, predictions)

    print(f"R2 Score: {score}")

    return score