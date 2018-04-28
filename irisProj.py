# Dragutin Sreckovic, 2018-04-01

# Python project on iris dataset

import pandas as pnd
import matplotlib.pyplot as mpl

dataFile = 'iris.csv'
dataSet = pnd.read_csv(dataFile)

for iris in dataSet['class'].unique():
    print(iris)

print(dataSet.groupby('class').size())

print(dataSet.describe())

irs = {}
for iris in dataSet['class'].unique():
    irs[iris] = dataSet[dataSet['class']==iris]
    print(irs[iris].describe())

dataSet.plot(kind="scatter", x="sepal_length", y="sepal_width")
mpl.show()

for i in irs:
    irs[i].plot(kind="hist", x="sepal_length", y="sepal_width")
    mpl.title(i)
    mpl.show()

dataSet.hist(edgecolor='black')
mpl.show()

pnd.plotting.scatter_matrix(dataSet)
mpl.suptitle('scatter-matrix')
mpl.show()
