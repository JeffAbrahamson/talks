"""A guided walk through seaborn's linear regression visualisaton functions.

Don't run this script or just copy and paste blindly.  Copy each small
section, then think about what it does, try some variations, ask
questions if you want.
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Seaborn assumes pandas dataframes.
tips = sns.load_dataset("tips")

# Exercise:  Look at tips.

# Basic plotting.
sns.lmplot("total_bill", "tip", tips)
plt.show()
# The confidence interval here was 95%.  We can change that.
sns.lmplot("total_bill", "tip", tips, ci=68)
plt.show()

# Seaborn supports discrete predictors as well.
sns.lmplot("size", "tip", tips);
plt.show()

# Jitter is useful for visualizing.
sns.lmplot("size", "tip", tips, x_jitter=.15)
plt.show()

# Maybe want the central tendency of each bin: use the x_estimator
# argument.  The estimator will be bootstrapped and a confidence
# interval will be plotted – 95% by default.
sns.lmplot("size", "tip", tips, x_estimator=np.mean)
plt.show()

# Exercise:  Play with the x_bins option.  It can be an array
# (explicit binning) or an int (number of bins).

# Hues let you see categorical data in different colors.
sns.lmplot("total_bill", "tip", tips, hue="smoker");
plt.show()

# Variant when color isn't enough.
sns.lmplot("total_bill", "tip", tips, hue="smoker", markers=["x", "o"]);
plt.show()

# Use columns instead of colors (changes emphasis).
sns.lmplot("total_bill", "tip", tips, col="smoker")
plt.show()

# Both color and columns.
sns.lmplot("total_bill", "tip", tips, col="smoker", hue="smoker")
plt.show()

# Go wild.  (Note:  This is kinda bad.)
g = sns.lmplot("total_bill", "tip", tips, hue="day", palette="Set2",
               hue_order=["Thur", "Fri", "Sat", "Sun"])
g.set_axis_labels("Total bill (US Dollars)", "Tip");
g.set(xticks=[10, 30, 50], ylim=(0, 10), yticks=[0, 2.5, 5, 7.5, 10]);
plt.show()

# No regression line.
sns.lmplot("total_bill", "tip", tips, hue="time", palette="Set1", fit_reg=False);
plt.show()

# Non-linear models.
sns.lmplot("size", "total_bill", tips, order=2)
plt.show()

# Logistic regression.
tips["big_tip"] = (tips["tip"] / tips["total_bill"]) > .15
sns.lmplot("total_bill", "big_tip", tips, y_jitter=.05)
plt.show()
sns.lmplot("total_bill", "big_tip", tips, y_jitter=.05, logistic=True)
plt.show()
# Exercise:  How separable are these sets really?

# Can bootstrap to try to be robust against outliers.
sns.lmplot("total_bill", "tip", tips, robust=True, n_boot=500)
plt.show()

# lmplot uses regplot, which is accessible directly when needed.
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
sns.regplot("total_bill", "tip", tips, ax=ax1)
sns.boxplot(tips["tip"], tips["size"], color="Blues_r", ax=ax2).set_ylabel("")
f.tight_layout()
plt.show()

# regplot also accepts numpy arrays.
x, y = np.random.multivariate_normal([1, 5], [(2, -.8), (-.8, 2)], 80).T
ax = sns.regplot(x, y, color="seagreen")
ax.set(xlabel="x variable", ylabel="y variable")
plt.show()

# The validity of linear regression depends, among other things, on
# the residuals being reasonable (normally distributed, etc.).
#
# With seaborn, we can view the residuals directly.
sns.residplot(x, y);
plt.show()

# Look at non-linear residuals.
y = x + 1.5 * x ** 2 + np.random.randn(len(x))
sns.residplot(x, y, color="indianred")
plt.show()

# Fit a Lowess curve to the residuals.
        sns.residplot(x, y, color="indianred", lowess=True)
plt.show()

# Check if a second order model might work.
sns.residplot(x, y, color="indianred", order=2, lowess=True)
plt.show()

# Plot marginal distributions.
sns.jointplot("total_bill", "tip", tips)
plt.show()

# With regression.
sns.jointplot("total_bill", "tip", tips, kind="reg", color="seagreen")
plt.show()

# Residuals.
sns.jointplot("total_bill", "tip", tips, kind="resid", color="#774499");
plt.show()
