#PREDICTIONS AND DATASET ARE BASED OFF OF ADULT AVERAGES IN THE USA!!!!!!
from sklearn import tree
from sklearn import svm
import numpy as np
#parsing and storing data in features
z = []
with open('features.txt', 'r') as xf:
    for xline in xf:
        x = xline.split(',')
        for i in range(0,len(x)):
            x[i] = int(x[i])
        z.append(x)
#parsing and storing data in labels
w = []
with open('labels.txt', 'r') as yf:
    for yline in yf:
        y = yline
        w.append(y)
#using Decision Tree Classifier algorithm
clf = tree.DecisionTreeClassifier()
#fitting both variables(features and labels) on graph
clf = clf.fit(z, w)
#inputting height in inches, weight in pounds, and shoe size(USA)
height = input("Enter your height in inches ")
weight = input("Enter your weight in pounds ")
shoesize = input("Enter your shoe size in USA standards ")
#predicting outcome using Decision Tree Classifier
prediction = clf.predict([[height, weight, shoesize]])
#outputting prediction
print("You are a ",prediction)
