# Dragutin Sreckovic, 2018-04-01

# Python project on iris dataset

# Importing packages:
import pandas as pnd
import matplotlib.pyplot as mpl
import seaborn as sb

##################################
## First some preparation work: ##
##################################

dataFile = 'iris.csv'               # File containing the dataset
dataSet = pnd.read_csv(dataFile)    # Reading it into Pandas dataframe
irs = {}                            # Dictionary for each Iris species dataset

# Separating dataset for each Iris species: 
j = 0
for iris in dataSet['class'].unique():
    irs[iris] = dataSet[dataSet['class'] == iris]
    j = j + 1


#######################################################################
## Defining now some useful functions for later use in the main part ##
#######################################################################

def showBasicStats():
    """ This function prints some basic statistics for the species. 
        For overall dataset and per species. """
    print("Iris overall stats:")
    print(dataSet.describe())       # Printing overall stats
    for i in irs:                   # Looping through species
        print('\n' + i + " stats:") # Printing 'header'
        print(irs[i].describe())    # Printing stats for the species 'i'

def otherInterestingStats():
    """ This function shows the following descriptive stats, 
        per species, of the dataset:
            min, max, mean, median, std, var, corr """
    statsList = ['min()', 'max()', 'mean()', 'median()', 'std()', 'var()', 'corr()']
    groupedDataset = dataSet.groupby('class')
    for s in statsList:
        print('\nApplying function ' + s + ':')
        print(eval('groupedDataset.' + s))
        
def psDistributionPlot():
    """ This function generates scatter petal & sepal distribution plot.
        Both plots are on the same picture. """
    plotTitle = ['Sepal Distribution','Petal Distribution'] # Plots' titles
    xCol = ['sepal_length', 'petal_length']                 # X-axis category
    yCol = ['sepal_width', 'petal_width']                   # Y-axis category
    clrs = ['r', 'b', 'g']                                  # List of colors to be used on the plot

    fig, ax = mpl.subplots(1, 2, figsize=(12, 6))           # Creating 2 subplots on the same figure
    for i in range(0, 2):   # Since we have 2 subplots
        j = 0               # Color counter
        for ir in irs:      # Looping through species and adding them to the graph
            irs[ir].plot(x=xCol[i], y=yCol[i], kind='scatter', ax=ax[i], label=ir, color=clrs[j])
            j = j + 1
        ax[i].set(title=plotTitle[i])   # Setting graph title
        ax[i].legend()                  # Adding legend to the graph
    mpl.show()


##################
###  Main part ###
##################

# Print basic stats about dataset:
showBasicStats()

# Print some additional interesting stats:
otherInterestingStats()

# Plot Sepal/Petal distribution:
psDistributionPlot()

# Pairplot graph:
sb.pairplot(dataSet, hue='class')
mpl.show()

# Radviz graph:
pnd.plotting.radviz(dataSet, 'class')
mpl.show()

