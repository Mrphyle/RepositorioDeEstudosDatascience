Create database empresa_rh;
use empresa_rh;

Create TABLE colaboradores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(120) NOT NULL, 
    cpf CHAR(11) NOT NULL UNIQUE,
    email VARCHAR(150) NOT NULL, 
    data_nascimento DATE NOT NULL,
    genero VARCHAR(20) NOT NULL,
    estado_civil VARCHAR(30) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    setor VARCHAR(80) NOT NULL, 
    cargo VARCHAR(80) NOT NULL, 
    data_admissao DATE NOT NULL,
    status VARCHAR(20) DEFAULT 'Ativo',
    Created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT INTO colaboradores(nome,cpf,email,data_nascimento,genero,estado_civil,salario,setor,cargo,data_admissao)
VALUES('Diego Simão Gonçalves','67676767676','diegosimaogoncalves18@gmail.com','2007-12-07','Masculino','Solteiro',10000,'Tecnico','Cientista de dados','2026-05-18');
--Insert
DELIMITER $$
CREATE TRIGGER Log_Acesso
AFTER INSERT ON colaboradores
FOR EACH ROW 
BEGIN
INSERT INTO Log_Acesso(usuario,acaso,data_acesso)
VALUES (USER(),CONCAT('INSERIU O FUNCIONARIO', NEW.id),NEW.nome,NOW());
END $$

DELIMITER ;

--Update
CREATE TRIGGER Update_log_Acesso
BEFORE UPDATE ON colaboradores
FOR EACH ROW
BEGIN
    SET NEW.status = 'Desativado';
END

--Delete
DELIMITER $$

CREATE TRIGGER log_deletados
AFTER DELETE ON colaboradores
FOR EACH ROW
BEGIN
    INSERT INTO log_exclusao (usuario_id, nome_antigo, data_remocao_colaborador)
    VALUES (OLD.id, OLD.nome, NOW());
END $$

DELIMITER ;