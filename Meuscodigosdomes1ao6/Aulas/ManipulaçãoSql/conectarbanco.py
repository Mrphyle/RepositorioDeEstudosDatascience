#baixar o xampp control painel v3.3.0
#abrir site http://localhost/phpmyadmin/ no site digite CREATE DATABASE mrphyle
def rascunho():
    '''CREATE TABLE Cliente (
        LocalFesta varchar(140),
        Telefone int(15),
        Nome varchar(85),
        id int(8) PRIMARY KEY
    );

    CREATE TABLE Items_da_festa (
        items_do_tema varchar(85),
        CorToalha varchar(15)
    );

    CREATE TABLE Tema_da_festa (
        Temas_disponiveis varchar(80)
    );

    CREATE TABLE Aluguel_Cliente_Items_da_festa_Tema_da_festa (
        fk_Cliente_id int(8)
    );
    
    ALTER TABLE Aluguel_Cliente_Items_da_festa_Tema_da_festa ADD CONSTRAINT FK_Aluguel_Cliente_Items_da_festa_Tema_da_festa_1
        FOREIGN KEY (fk_Cliente_id)
        REFERENCES Cliente (id)
        ON DELETE NO ACTION;'''
import mysql.connector as sqc
try:
    conexção = sqc.connect(
        host = 'localhost',
        user = 'root',
        password = "",
        database = 'test',
    )
    print("conectado com susseso!")
except:
    print("Não foi possivel se conectar")
finally:
    conexção.close()
