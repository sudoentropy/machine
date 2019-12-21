import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as pyplot
import pickle #pickle is used to save trained model
from matplotlib import style


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

"""
#automating the process to train a mode with high accuracy with a for loop
best = 0
for _ in range(1000):

    #this was left in here only for clean code
    #duplicate above may not serve functional purpose
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    #fitting data to a linear model
    linear = linear_model.LinearRegression()

    #create a model and test its accuracy
    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    #if statement to kill for loop
    if accuracy > best:
        best = accuracy

        #section commented out that saves the model
        #saving trained model
        with open("grade_pred_model.pickle", "wb") as f:
            pickle.dump(linear, f)"""

#defining variable.....i believe, probably incorrect prog term but whatevs
pickle_in = open("grade_pred_model.pickle", "rb")

#loading saved pickle into linear model
linear = pickle.load(pickle_in)

#5dimensional linear models coeffficients
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

#ai prediction
predictions = linear.predict(x_test)

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])

#visualization
p = 'G1'
style.use("ggplot")
pyplot.scatter(data[p], data["G3"])
pyplot.xlabel(p)
pyplot.ylabel("Final Grade (G3)")
pyplot.show()
