"""
connecting sql alchemy to local sqlserver
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

# essentially a head test
# df = pd.read_sql_query(
#     "select top 10 * from [csv_test].[dbo].[human_liver]",
#     connection)
# print(df)

# # will see if engine and connection do the same thing
# df = pd.read_sql_table("human_liver", engine)
# print(df.head())

# test with "connection" method
df= pd.read_sql_table("human_liver", connection)
print(df.head())

# connection is probably more correct way to do this shiiiit

