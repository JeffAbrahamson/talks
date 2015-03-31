#!/usr/bin/python3

"""
Demo of Anscombe's quartet in Python
Prints the return values from linregress to show that they're all identical
https://en.wikipedia.org/wiki/Anscombe's_quartet

Kudos: https://gist.github.com/endolith/3299951
"""
 
from matplotlib.pyplot import subplot, scatter, plot, axis, show
from scipy.stats import linregress
 
x1 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
 
x2 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
 
x3 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
 
x4 = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0]
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
 
xmax = 20
ymax = 14
 
ax1 = subplot(2, 2, 1)
scatter(x1, y1)
slope, intercept, r_value, p_value, std_err = linregress(x1, y1)
plot([0, xmax], [intercept, slope * xmax + intercept])
print("{0:.3f} {1:.2f} {2:.3f} {3:.3f} {4:.3f}".format(slope, intercept, r_value, p_value, std_err))
 
subplot(2, 2, 2, sharex=ax1, sharey=ax1)
scatter(x2, y2)
slope, intercept, r_value, p_value, std_err = linregress(x2, y2)
plot([0, xmax], [intercept, slope * xmax + intercept])
print("{0:.3f} {1:.2f} {2:.3f} {3:.3f} {4:.3f}".format(slope, intercept, r_value, p_value, std_err))
 
subplot(2, 2, 3, sharex=ax1, sharey=ax1)
scatter(x3, y3)
slope, intercept, r_value, p_value, std_err = linregress(x3, y3)
plot([0, xmax], [intercept, slope * xmax + intercept])
print("{0:.3f} {1:.2f} {2:.3f} {3:.3f} {4:.3f}".format(slope, intercept, r_value, p_value, std_err))
 
subplot(2, 2, 4, sharex=ax1, sharey=ax1)
scatter(x4, y4)
slope, intercept, r_value, p_value, std_err = linregress(x4, y4)
plot([0, xmax], [intercept, slope * xmax + intercept])
print("{0:.3f} {1:.2f} {2:.3f} {3:.3f} {4:.3f}".format(slope, intercept, r_value, p_value, std_err))
 
axis([0, xmax, 0, ymax])
# show()
