# Dragutin Sreckovic, 2018-04-01

# Python project on iris dataset

# Importing packages:
import pandas as pnd
import matplotlib.pyplot as mpl

def showBasicStats():
    """ This function prints some basic statistics for the species """
    print("Iris overall:")
    print(dataSet.describe()) # overall stats
    for i in irs:
        print()
        print(i + ":")
        print(irs[i].describe()) # stats for the species i

def distributionPlot(plotTitle,xCol,yCol):
    """ This function generates scatter distribution plot """
    mpl.figure()
    fig,ax=mpl.subplots(1,1,figsize=(12, 6))
    for i in irs:
        irs[i].plot(x=xCol, y=yCol, kind="scatter", ax=ax, label=i,color=irsColors[i])
    ax.set(title=plotTitle)
    ax.legend()
    mpl.show()

# File containing the dataset:
dataFile = 'iris.csv'
# Reading it into Pandas dataframe:
dataSet = pnd.read_csv(dataFile)

# Initialising dictionaries I'll use to loop through Iris species:
irs = {} # dictionary for each Iris class dataset:
irsColors = {}  # dictionary that holds species-color relation 

# List of colors to be used:
clrs = ['r','b','g']

# Separating dataset for each Iris species and assigning it a color: 
j = 0
for iris in dataSet['class'].unique():
    irs[iris] = dataSet[dataSet['class']==iris]
    irsColors[iris] = clrs[j]
    j = j + 1

# Printing basic stats:
showBasicStats()
# Plot Sepal distribution:
distributionPlot('Sepal comparasion','sepal_length','sepal_width')
# Plot Petal distribution:
distributionPlot('Petal Comparasion','petal_length','petal_width')
