import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# Importing the dataset
data = pd.read_csv('LinearRegressionPoly_Data.csv')
print(data)
print(data.shape)    #(7,2)
X = data.iloc[ : , 0:1].values    # [ rows , cols ]
y = data.iloc[ : , 1].values      # [ rows , cols ]
print("X.shape = ", X.shape , "\n X=\n" , X )
print("y.shape = ", y.shape , "\n y=" , y )

lin = LinearRegression()
lin.fit(X, y)  # estimate the parameters of the model

# Predictions
y_dash = lin.predict(X)

# Plot the data points
plt.scatter(X, y, color='blue')      # original points
plt.scatter(X, y_dash, color='m')    # predicted points

# Plot regression line
plt.plot(X, y_dash, color='red')

# Labels and title
plt.title('Linear Regression')
plt.xlabel('Engine Temperature')
plt.ylabel('Engine Pressure')

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

poly = PolynomialFeatures(degree=8)
X_poly = poly.fit_transform(X)
print('X = \n', X)
print('X_poly = \n', X_poly)

lin2 = LinearRegression()
lin2.fit(X_poly, y)

plt.scatter(X, y, color='blue')
y_pred = lin2.predict(X_poly)
plt.plot(X, y_pred, color='red')
plt.title('Polynomial Regression')
plt.xlabel('Engine Temperature')

# Show plot
plt.show()

print("LinearRegression: ", lin.predict([[110.0]]))
print("PolyRegression: ", lin2.predict(poly.fit_transform([[110.0]])))