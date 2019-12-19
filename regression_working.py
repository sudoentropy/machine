import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

#read data into pandas dataframe, sep is listing delinieator
data = pd.read_csv("student-mat.csv", sep=";")

#select desired attributes
data = data[["G1", "G2", "G3", "studytime", "absences", "failures"]]

#predict maybe called "label"
predict = "G3"

#set up 2 arrays
#labels array
X = np.array(data.drop([predict], 1))
#features array
y = np.array(data[predict])

#splitting into training and 10% testing data
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

#fitting data to a linear model
linear = linear_model.LinearRegression()

#create a model and test its accuracy
linear.fit(x_train, y_train)
accuracy = linear.score(x_test, y_test)
print(accuracy)