import pandas
# Load pandas, read this
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
import matplotlib.pyplot as plt
import numpy as np


def plot(x, y):
    plt.plot(x, y)
    plt.show()


# load CSV as a pandas data frame obj
df = pandas.read_csv('../data/College.csv')

# .head() returns the top few rows of a data frame
print(df.head())
# .columns shows the columns names
print(df.columns)

# question 8ci
# R summary is equivalent to pandas describe
print(df.describe())

# question 8cii
# scatter
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
scatter = pandas.plotting.scatter_matrix(df.loc[:,'Apps':'Top25perc'])
fig = scatter[0,0].get_figure()
fig.savefig("../plots/lab1/scatter.pdf")

