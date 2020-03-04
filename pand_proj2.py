"""
connecting to local sql server then reading and understanding the data
"""


import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
import pandas_profiling


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


df = pd.read_sql_table("human_liver", connection)
# print(df.describe)
# print(df.corr)

ext_report = pandas_profiling.ProfileReport(df)

# line not complete, need an export path
# ext_report.to_file("C:/")
