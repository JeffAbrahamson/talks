#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
X = 5 * np.arange(num_points) + np.random.random_sample(num_points)
Y = 7 + 2 * X + 3 * np.random.normal(0, 1, num_points)

plt.title('Y plotted against X')
plt.xlabel("x's in parsecs")
plt.ylabel("Y's in lightyears")
plt.plot(X, y, 'b.')
plt.grid(True)
plt.show()

from sklearn.linear_model import LinearRegression
Xsk = [[x] for x in X]
Ysk = [[x] for x in Y]
model = LinearRegression()
model.fit(Xsk, Ysk)
# All estimators in scikit-learn implement fit() and predict().
print("Your x is {x:.1f} parsecs, that's going to mean a y of about {y:.1f} lightyears.".format(
    x=10, y=model.predict(10)[0][0]))

# Compute residual sum of squares.
print("The residual error is {err:.2f}.".format(
    err=np.mean((model.predict(X) - y) **2)))
print("Var(X) = {var:.2f}.".format(
    var=np.var(X, ddof=1)))

# Cf. also:
model.coef_
model.intercept_

residuals_sk = [model.predict(Xsk) - Ysk][0]
# or
residuals = [x[0] for x in [model.predict(X) - y][0]]

# Now plot the residuals
plt.plot(X, residuals, 'bo')
plt.show()

# Now histogram the residuals
plt.hist(residuals, bins=10)
plt.show()

plt.hist(residuals, bins=10, cumulative=True)
plt.show()

# Exercise: Do this with 500 or 5000 samples and play with plotting functions..
# Exercise: Increase the noise.  Try a different noise (residual) distribution.
plt.plot(X, Y, 'bo')
x_points = np.linspace(min(X), max(X), num=num_points)
y_points = [model.intercept_[0] + model.coef_[0] * x
            for x in x_points]
plt.plot(x_points, y_points, 'r-')
plt.show()
