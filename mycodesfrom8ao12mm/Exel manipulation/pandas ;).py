import pandas as pd
import mysql.connector as msql
from sqlalchemy import create_engine
def xlstosql(excel_file, sheet_name, db_name, table_name):
    try:
        df = pd.read_excel(excel_file, sheet_name=sheet_name)
        conn = msql.connect(host="localhost",
                            user="root",
                            password="",
                            database=db_name)
        engine = create_engine(f'mysql+mysqlconnector://root:@localhost/{db_name}')
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    except:
        print('Erro')
 
arquivo = 'bdexcel.xlsx'
banco = 'ruby'
tabela = 'aluno'
xlstosql(arquivo,banco,tabela)