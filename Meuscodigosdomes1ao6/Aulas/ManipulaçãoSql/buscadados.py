import mysql.connector as sqc
import pandas as pd
config = {
    'user':'root',
    'password':'',
    'host': 'localhost',
    'database': 'mrphyle'
}
conect = sqc.connect(**config)
query = "SELECT * FROM"
df = pd.read_sql_query(query, conect)
print("Dados lidos do banco de dados:")
print(df.head())

# Fechando a conexão
conect.close()