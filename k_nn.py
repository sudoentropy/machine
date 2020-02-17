import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

#importing data
data = pd.read_csv("Breast_GSE.csv")

# checks data import
# print(data.head())

# preprocesses any str data into ints for future computation
le = preprocessing.LabelEncoder()
type = le.fit_transform(list(data["type"]))
print(type)

predict = "type"

x =
y =