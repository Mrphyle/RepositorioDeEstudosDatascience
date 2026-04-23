CREATE DATABASE ruby2304;
USE ruby2304;

CREATE TABLE aluno (id int(11) NOT NULL,nome varchar(100) NOT NULL,curso varchar(100) NOT NULL,idade int(11) NOT NULL,cidade int(11) NOT NULL
);
INSERT INTO aluno (id, nome, curso, idade, cidade) VALUES
(1, 'Diogo Silva', 'Ciência de dados', 17, 1),
(2, 'João Gabriel', 'Ciência de dados', 17, 1),
(3, 'Matheus Pessete', 'Ciências da computação', 21, 2),
(5, 'Eliandro Brandão Spada', 'Mestrado em computação', 45, 3);

CREATE TABLE cidade(id int(11) NOT NULL, nome varchar(100) NOT NULL);

INSERT INTO cidade(id, nome) VALUES
(1, 'São José do Rio Preto'),
(2, 'Mirassol'),
(3, 'Catanduva');

CREATE VIEW vwAlunosCompleto AS SELECT aluno.nome, aluno.curso, cidade.nome AS Cidade FROM aluno,cidade WHERE aluno.cidade = cidade.id;

CREATE VIEW vwconsulta AS SELECT * FROM aluno;

SELECT * FROM vwconsulta;

ALTER VIEW vwconsulta AS SELECT nome, curso FROM aluno;

DROP VIEW vwconsulta;