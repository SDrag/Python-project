# Python-project

## Content
File Name | Comment 
--------- | -------
Figure_1.png | Sepal/Petal distribution graph
Figure_2.png | Pairplot graph	
Figure_3.png | Radviz graph
Table_1.png | Screenshot of ```showBasicStats()``` function output
Table_2a.png | Screenshot of the first part of ```otherInterestingStats()``` function output
Table_2b.png | Screenshot of the second part of ```otherInterestingStats()``` function output
iris.csv | Iris dataset
irisProj.py | Python project script

## Summary
Fisher's Iris data set[[2](https://archive.ics.uci.edu/ml/datasets/iris)] is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper "The use of multiple measurements in taxonomic problems" as an example of linear discriminant analysis[[1](https://en.wikipedia.org/wiki/Iris_flower_data_set)].
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor) and reports on 4 characteristics of each of them: sepal length, sepal width, petal length, and petal width, in centimetres. 

It is often used in statistical science for illustrating various problems in statistical graphics, multivariate statistics and machine learning.
Containing 150 observations, it is small but not trivial and the task it poses of discriminating between 3 species from measurements of their petals and sepals is simple yet challenging.

I demonstrate here basic statistical analysis of the Iris dataset in python, using pandas, seaborn and matplotlib packages.




## Examples of some interesting analyses on the data set
examples of interesting analyses that others have pursued based on the data set

## Code documentation
To run the code, in a terminal type: ```python irishProj.py```

In the script, I first import dataset file and set some variables I use later in the code.

Then I define few functions:
-  ```showBasicStats()``` - prints some basic stats (minimum, maximum, mean, standard deviation, ...) using pandas'  **describe()** function
-  ```otherInterestingStats()``` - using pandas' **min(),max(),mean(),median(),std(),var(),corr()** functions in a loop on grouped dataframe
-  ```psDistributionPlot()``` - generates a picture with 2 graphs showing petal and sepal distribution (scatter plot)

In the main part of the script, I call above mentioned functions and also create *pairplot* and *radviz graphs*. 

## References
[1] https://en.wikipedia.org/wiki/Iris_flower_data_set

[2] https://archive.ics.uci.edu/ml/datasets/iris

[3] http://www.learn4master.com/machine-learning/visualize-iris-dataset-using-python

[4] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

[5] https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching

[6] http://patrickhoey.com/downloads/Computer_Science/03_Patrick_Hoey_Data_Visualization_Dataset_paper.pdf

[7] http://pandas.pydata.org/

[8] https://seaborn.pydata.org

[9] https://matplotlib.org/
