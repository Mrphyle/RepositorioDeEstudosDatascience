import mysql.connector
from   mysql.connector import Error
from datetime import datetime
import requests
try:
    conexao = mysql.connector.connect(
        host='localhost',        # ou IP do servidor
        user='root',
        password='',
        database='cotacao'
    )
    valor_ask = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL").json()["USDBRL"]["ask"]

    if conexao.is_connected():
        print("Conectado ao MySQL com sucesso!")

    sql = """
        INSERT INTO cotacao (data_hora, valor)
        VALUES (%s, %s)
    """
    cursor = conexao.cursor()
    data_hora = datetime.now()
    valores = (data_hora, valor_ask)
    cursor.execute(sql, valores)
    conexao.commit()
except Error as e:
    print("Erro ao conectar no MySQL:", e)

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")