"""
Mega ML 34:26
"""


import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures",
             "absences"]]

predict = "G3"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, y_train, x_test, y_test, = sklearn.model_selection.train_test_split(
    X, y, test_size=0.1)
