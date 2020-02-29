"""
connecting sql alchemy to local sqlserver


have learned how to connect to sql server
use sqlalchemy to talk to server
some pyodb i guess because certain method would not work without it
also have learned to reference select columns
"""


import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# connecting to local sql database, this code below works 2-28-20
SERVER = 'ETHINK'
DATABASE = 'csv_test'
DRIVER = 'SQL Server Native Client 11.0'
USERNAME = ''
PASSWORD = ''
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

# engine is the db connection method, mthinks
engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

# essentially a head test, with sqly language and shiiiite
# df = pd.read_sql_query(
#     "select top 10 * from [csv_test].[dbo].[human_liver]",
#     connection)
# print(df)

# # will see if engine and connection do the same thing
# df = pd.read_sql_table("human_liver", engine)
# print(df.head())

# test with "connection" method
# connection is probably more correct way to do this shiiiit

# this is referencing only the column genes
# df= pd.read_sql_table("human_liver", connection, columns=['genes'])
# print(df.head())

# df = pd.read_sql_table("human_liver", connection, columns=['genes', 'GSM2055788'])
# print(df)

# this is loading the whole df
df = pd.read_sql_table('human_liver', connection)
# print(df.head())

index = df.index
print(index)

columns = df.columns
print(columns)

values = df.values
print(values)
