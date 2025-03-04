import mysql.connector as sqc
import pandas as pd
import os
Marca = input("Digite o nome da marca: ")
tipo_do_produto = input("Digite o tipo do produto: ")
Codigo_de_barras = int(input("Digite o codigo de barras do produto: "))
descricao = input("faça a descrição do produto: ")
valor = float(input("Digite o valor: "))
try:
    connection = sqc.connect(
        host='localhost',
        user='root',
        password='',
        database='test',
    )
    cursor = connection.cursor()
    
    #Cria comando SQL com placeholders
    comand_sql = """
    INSERT INTO produtos (Marca, tipo_do_produto, Codigo_de_barras, descricao, valor) 
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(comand_sql, (Marca, tipo_do_produto, Codigo_de_barras, descricao, valor))
    connection.commit()
    print("Registro inserido com sucesso.")
except sqc.Error as err:
    print(f"Erro ao se conectar ao banco de dados: {err}")
finally:
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()