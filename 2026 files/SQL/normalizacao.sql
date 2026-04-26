/*tabelas*/
CREATE TABLE aluno (
    id_aluno INT PRIMARY KEY,
    nome_aluno VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    cpf VARCHAR(14) UNIQUE,
    email VARCHAR(100) UNIQUE,
    telefone VARCHAR(20),
    endereco VARCHAR(150),
    id_sala INT,
    FOREIGN KEY (id_sala) REFERENCES sala(id_sala)
);

CREATE TABLE curso (
    id_curso INT PRIMARY KEY,
    nome_curso VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL
);

CREATE TABLE sala (
    id_sala INT PRIMARY KEY,
    nome_sala VARCHAR(50) NOT NULL,
    id_curso INT,
    FOREIGN KEY (id_curso) REFERENCES curso(id_curso)
);

/*inserções*/

INSERT INTO aluno VALUES
(1, 'Carlos Silva', '2006-03-15', '123.456.789-00', 'carlos.silva@email.com', '(17) 99999-1111', 'Rua A, 123', 1),
(2, 'Ana Souza', '2005-07-22', '987.654.321-00', 'ana.souza@email.com', '(17) 98888-2222', 'Rua B, 456', 2),
(3, 'João Pereira', '2007-01-10', '111.222.333-44', 'joao.p@email.com', '(17) 97777-3333', 'Rua C, 789', 1),
(4, 'Mariana Costa', '2004-11-30', '555.666.777-88', 'mariana.c@email.com', '(17) 96666-4444', 'Av. Central, 100', 3),
(5, 'Pedro Almeida', '2006-05-18', '999.888.777-66', 'pedro.a@email.com', '(17) 95555-5555', 'Rua D, 321', 4);

INSERT INTO curso VALUES
(1, 'Informática', 1200),
(2, 'Administração', 1000),
(3, 'Enfermagem', 1800);

INSERT INTO sala VALUES
(1, 'Sala A', 1),
(2, 'Sala B', 2),
(3, 'Sala C', 3),
(4, 'Sala D', 1);

/*views*/

-- View 1: Aluno + Sala
CREATE VIEW vwAlunoSala AS
SELECT aluno.nome_aluno, aluno.email, aluno.telefone, sala.nome_sala 
FROM aluno, sala 
WHERE aluno.id_sala = sala.id_sala;

-- View 2: Aluno + Curso
CREATE VIEW vwAlunoCurso AS
SELECT aluno.nome_aluno, aluno.email, curso.nome_curso, curso.carga_horaria
FROM aluno, sala, curso
WHERE aluno.id_sala = sala.id_sala AND sala.id_curso = curso.id_curso;

-- View 3: Aluno + Sala + Curso
CREATE VIEW vwAlunoSalaCurso AS
SELECT aluno.nome_aluno, aluno.email, aluno.telefone, sala.nome_sala, curso.nome_curso, curso.carga_horaria
FROM aluno, sala, curso
WHERE aluno.id_sala = sala.id_sala AND sala.id_curso = curso.id_curso;

-- View Anonimização de Dados COMO CPF, email e telefone dos alunos.
CREATE VIEW vwAlunoAnonimizado AS
SELECT 
    aluno.id_aluno,
    aluno.nome_aluno,
    CONCAT(SUBSTRING(aluno.cpf, 1, 3), '.***.**') AS cpf_mascarado,
    CONCAT('***@', SUBSTRING(aluno.email, POSITION('@') IN aluno.email + 1)) AS email_mascarado,
    CONCAT('(17) ****-', RIGHT(aluno.telefone, 4)) AS telefone_mascarado,
    sala.nome_sala,
    curso.nome_curso
FROM aluno, sala, curso
WHERE aluno.id_sala = sala.id_sala AND sala.id_curso = curso.id_curso;