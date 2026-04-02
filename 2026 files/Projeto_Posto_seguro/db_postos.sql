Create DATABASE Posto_seguro
Create table Cadastros(id int Primary Key auto_increment,Nome_usuario Varchar(25), Email varchar(75),Senha varchar(50))
Create table Postos_Cadastrados(Localização,varchar(250),qualidade_combustivel varchar(9),Valor_Etanol int, Valor_Gasolina int, Valor_GNV INT,Valor_Diesel int, id_usuario int, FOREIGN KEY (id_usuario) REFERENCES Cadastros(id))

/*exemplo de dados*/
INSERT INTO Cadastros(Nome_usuario,Email,Senha) VALUES ("Diego Simão","slenderk54@gmail.com","zezinho123");



