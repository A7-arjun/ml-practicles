##python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
X = np.array([[1], [2], [3], [4], [5]])
Y = np.array([20, 30, 40, 50, 60])
print("studyhr", X)
print("marks", Y)
model = LinearRegression()
model.fit(X, Y)
print("model trained successfully")
prediction = model.predict([[6]])
print("predicted marks for 6 hours of study:", prediction)
print("model coefficients:", model.coef_)
print("model intercept:", model.intercept_)

plt.scatter(X, Y)
plt.plot(X, model.predict(X))
plt.title("linear regression")
plt.xlabel("study hours")
plt.ylabel("marks")
plt.legend(["predicted line", "actual data"])
plt.show()
