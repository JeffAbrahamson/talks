#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import sklearn
from sklearn import linear_model

## Pizza model ############################################################

Diametre = [[6], [9], [12], [15], [18], [30]]
prix = [[7], [9], [13], [17.5], [18], [24]]
plt.figure()
plt.title('Pizza v diametre')
plt.xlabel('Diametre (cm)')
plt.ylabel(u'Prix (€)')
plt.plot(Diametre, prix, 'k.')
plt.axis([0, 32, 0, 25])
plt.grid(True)
plt.show()

pizza_model = linear_model.LinearRegression()
pizza_model.fit(Diametre, prix)
print(pizza_model.intercept_, pizza_model.coef_)
print('J(theta) = {ss:.1f}'.format(ss=sum([(y - pizza_model.predict(x))**2 for x,y in zip(Diametre, prix)])[0]))

plt.scatter(Diametre, prix, color='black')
plt.scatter(25, pizza_model.predict(25), color='red')
plt.plot(Diametre, pizza_model.predict(Diametre), color='blue')
plt.show()

a = pizza_model.intercept_[0]
b = pizza.coef_[0][0]
[a + b * x[0] for x in Diametre]
