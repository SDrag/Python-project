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
    
 
