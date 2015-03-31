#!/usr/bin/python3

import matplotlib.pyplot as plt
X = [6.2, 8.9, 11, 15, 22]
y = [7, 8.2, 14.1, 17.5, 20.1]
plt.figure()
plt.title('Y plotted against X')
plt.xlabel("x's in parsecs")
plt.ylabel("Y's in lightyears")
plt.plot(X, y, 'b.')
plt.axis([0, 25, 0, 25])
plt.grid(True)
plt.show()

from sklearn.linear_model import LinearRegression
X = [[x] for x in X]
y=[[x] for x in y]
model = LinearRegression()
model.fit(X, y)
# All estimators in scikit-learn implement fit() and predict().
print("Your x is {x:.1f} parsecs, that's going to mean a y of about {y:.1f} lightyears.".format(
    x=10, y=model.predict(10)[0][0]))

import numpy as np
# Compute residual sum of squares.
print("The residual error is {err:.2f}.".format(
    err=np.mean((model.predict(X) - y) **2)))
print("Var(X) = {var:.2f}.".format(
    var=np.var(X, ddof=1)))
