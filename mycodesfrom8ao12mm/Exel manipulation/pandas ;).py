#CREATE TABLE funcionarios(id int, nome varchar(70), cidade varchar(70), datanacimento varchar(15));
#resolvesql or sonvesql
import pandas as pd
import mysql.connector as msc
from sqlalchemy import crea
try:
    conn = msc.connect(
        host="localhost",
        user="root",
        password=""
        databese="pandinha"
    )
    index = pd.read_excel("bdexel.xlsx",sheet_name="Planilha1")
except:
    print("ERROR!!!")