import pandas as pd 
import sqlite3 as sql
#
def xls_to_sql(exel_file,sheet_name,db_name,table_name):
    df = pd.read_excel(exel_file,sheet_name=sheet_name)
    conn = sql.connect(db_name)
    df.to_sql(table_name, conn, if_exists="replace",index=False)
    conn.close
    print(f"Crated table {table_name} in {db_name}.")

file = "bdexcel.xlsx"
sheet = "spreadsheet1"
database = "databese.slite3" 
table = "student"
xls_to_sql(file,sheet,database,table)