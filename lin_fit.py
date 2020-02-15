"""
Mega ML 34:26
"""


import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read__csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures",
             "absences"]]

predict = "G3"

x = np.array(data.drop([predict], 1))

x_train, y_train, x_test, y_test, = sklearn.model_selection.train_test_split(
    X, y, test_size=0.1)
