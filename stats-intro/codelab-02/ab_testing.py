#!/usr/bin/python3

import scipy.stats as ss
import statsmodels.graphics.boxplots as smgb

def get_51():
    x = ss.norm.rvs(size=1000, loc=17)
    y = ss.norm.rvs(size=1000, loc=17.1)
    return x, y

def compute_p(x, y):
    print(ss.ttest_rel(x, y))

def plot_box(x):
    plt.boxplot(x)
    plt.show()

def plot_violin(x, y):
    smgb.violinplot([x, y])
    plt.show()

def plot_bean(x, y):
    smgb.beanplot([x, y])
    plt.show()

def kstest(x):
    """Kolmogorov-Smirnov test."""
    print(ss.kstest(x, 'norm'))

def ks2s(x, y):
    print(ss.ks_2samp(x, y))
    # Consider values like this:
    # x = ss.norm.rvs(size=1000)
    # y = ss.norm.rvs(size=1000)
    # y = ss.norm.rvs(size=1000) + .01 * ss.norm.rvs(size=1000)
    # y = ss.norm.rvs(size=1000) + ss.norm.rvs(size=1000)

# Exercise:  Construct time series, new feature started at time t_0.

# Exercise: Construct time series, new feature started at time t_0.
# We've noticed time of day behavior modeled by sin(minute_of_day /
# 1440).
