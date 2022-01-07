import pandas as pd
import pyodbc 
from sqlalchemy import create_engine
import urllib.parse
password=urllib.parse.quote("Sudha@506")
host='DESKTOP-2M7LE50\SUDHAMSSQL'
c=f"mssql+pyodbc://sa:{password}@{host}/stage_db?driver=SQL+Server"
conn=create_engine(c)

df = pd.read_sql('SELECT * FROM stdata', conn)

print(df)
