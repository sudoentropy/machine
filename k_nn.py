import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

#importing data
data = pd.read_csv("clinvar.csv", sep=",")

# checks data import
# print(data.head())


# preprocesses any str data into ints for future computation
le = preprocessing.LabelEncoder()

chrom = le.fit_transform(list(data["CHROM"]))

ref = le.fit_transform(list(data["REF"]))

alt = le.fit_transform(list(data["ALT"]))

cldn = le.fit_transform(list(data["CLNDN"]))

clnhgvs = le.fit_transform(list(data["CLNHGVS"]))

clnvc = le.fit_transform(list(data["CLNVC"]))

mc = le.fit_transform(list(data["MC"]))

consequence = le.fit_transform(list(data["Consequence"]))

impact = le.fit_transform(list(data["IMPACT"]))

symbol = le.fit_transform(list(data["SYMBOL"]))

feature = le.fit_transform(list(data["Feature_type"]))

biotype = le.fit_transform(list(data["BIOTYPE"]))

exon = le.fit_transform(list(data["EXON"]))

intron = le.fit_transform(list(data["INTRON"]))

aminoa = le.fit_transform(list(data["Amino_acids"]))

codons = le.fit_transform(list(data["Codons"]))

bamedit = le.fit_transform(list(data["BAM_EDIT"]))

sift = le.fit_transform(list(data["SIFT"]))

polyophen = le.fit_transform(list(data["PolyPhen"]))

motifn = le.fit_transform(list(data["MOTIF_NAME"]))

highip = le.fit_transform(list(data["HIGH_INF_POS"]))

predict = "CHROM"

x = list(zip(ref, alt, cldn, clnhgvs, clnvc, mc, consequence, impact, symbol, feature, biotype, exon, intron, aminoa, codons, bamedit, sift, polyophen, motifn))
y = list(chrom)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    x, y, test_size=0.1)

print(x_train, y_test)

model = KNeighborsClassifier(n_neighbors=1)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

