from src.train import train_model
from src.evaluate import evaluate_model

model, X_test, y_test = train_model()

score = evaluate_model(model, X_test, y_test)

print("Model training completed")