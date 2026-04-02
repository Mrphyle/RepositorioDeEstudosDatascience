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