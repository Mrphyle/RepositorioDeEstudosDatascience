import pandas as pd 
import sqlite3 as sql
import mysql.connector as msc
from sqlalchemy import create_engine
#
def xls_to_sql(exel_file,sheet_name,db_name,table_name):
    try:
        df = pd.read_excel(exel_file,sheet_name=sheet_name)
        df.to_sql(table_name, conn, if_exists="replace",index=False)
        conn = msc.connect(
            host="localhost",
            user="root",
            password="",
            databese="pandinha")
        index = pd.read_excel("bdexel.xlsx",sheet_name="Planilha1")
    except:
        print("ERROR!!!")

file = "bdexcel.xlsx"
sheet = "Planilha1"
database = "databese.slite3" 
table = "student"
xls_to_sql(file,sheet,database,table)