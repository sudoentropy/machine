"""
taking lead of gene researchers
dumping most of the data to find important unique patterns
Assumption: probably most of it is false patterns
"""


import pandas as pd


df = pd.read_csv('Brain_GSE5.csv')

# transposing the data because it has 50,000 columns of genes
# maybe the genes are the data, not the features???
df_t = df.T




