import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

#importing data
data = pd.read_csv("Breast_GSE.csv", sep=",")

# checks data import
# print(data.head())

# preprocesses any str data into ints for future computation
le = preprocessing.LabelEncoder()
type = le.fit_transform(list(data["type"]))
print(type)

predict = "type"

x = list(zip(A2-A0CM.07TCGA,	BH-A18U.08TCGA,	A2-A0EQ.08TCGA,	AR-A0U4.09TCGA,	AO-A0J9.10TCGA,	AR-A1AP.11TCGA,	AN-A0FK.11TCGA,	AO-A0J6.11TCGA,	A7-A13F.12TCGA,	BH-A0E1.12TCGA
))
y = list(type)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, test_size=0.1)

print(x_train, y_test)

# pick it up at 1:07 with another simpler dataset
# this dataset is too complex atm



