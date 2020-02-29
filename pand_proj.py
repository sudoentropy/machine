"""
connecting sql alchemy to local sqlserver
"""


import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

# connecting to local sql database
SERVER = 'ETHINK'
DATABASE = 'csv_test'
DRIVER = 'SQL Server Native Client 11.0'
USERNAME = ''
PASSWORD = ''
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

df = pd.read_sql_table("genes", engine)
print(df)