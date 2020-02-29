"""
taking lead of gene researchers
dumping most of the data to find important unique patterns
Assumption: probably most of it is false patterns
"""


import pandas as pd
import sqlalchemy

# connecting to local sql database
engine = sqlalchemy.create_engine('mysql+pymysql://root:@127.0.0.1:1433/csv_test')

df = pd.read_sql_table("genes", engine)
print(df)