import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing


# importing data
data = pd.read_csv("car.data", sep=",")

# checks data import
# print(data.head())


# preprocesses any str data into ints for future computation
le = preprocessing.LabelEncoder()

Buying = le.fit_transform(list(data["Buying"]))
MAINT = le.fit_transform(list(data["MAINT"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

x = list(zip(Buying, MAINT, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, test_size=0.1)

# dataset was not too complex, it was just loaded wrong
# le processing was not used correctly
# seems like every column must be preprocessed
# also the tags loading into zip are the identifiers, not the column headers

# takes one paramter: number of neighbors
# hyperparamter: means you tweak it as you train
model = KNeighborsClassifier(n_neighbors=5)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)







