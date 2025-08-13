import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def get_training_data(filename):
    # Code to read CSV file and return x, y
    import pandas as pd
    data = pd.read_csv(filename)
    x = data.iloc[:, :-1].values
    y = data.iloc[:, -1].values
    return x, y

def train_linear_model(x_parameters, y_parameters, quest_value):
    # Train model
    model = LinearRegression()
    model.fit(x_parameters, y_parameters)
    prediction = model.predict([[quest_value]])
    print(f"Predicted value for {quest_value} is {prediction[0]}")

def startAIAlgorithm():
    # Collect the training data from external csv data file.
    x, y = get_training_data('LR_House_price.csv')
    print("Formatted Training Data : ")
    print("x = ", x)
    print("y = ", y)
    question_value = 700  # This is the question
    train_linear_model(x, y, question_value)

startAIAlgorithm()
