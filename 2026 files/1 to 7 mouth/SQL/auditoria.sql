Create database auditoria;
Use auditoria;

/* Table users */
Create table users(
    id_user INT PRIMARY KEY, 
    name varchar(100) not null, 
    department varchar(100) not null, 
    Perfil varchar(100) not null, 
    status_user varchar(100) not null
);

/* Tables logs */
Create table log_acess (
    id_log INT PRIMARY KEY, 
    id_user INT, 
    data_acesso datetime, 
    ip_origem varchar(50), 
    system varchar(100),
    status_login varchar(20) not null, 
    foreign key (id_user) references users(id_user)
);

create table logs_operacoes (
    id_operacao INT PRIMARY KEY, 
    id_user INT, 
    data_operacao datetime, 
    tipo_operacao varchar(50), 
    tabela_afetada varchar(100), 
    tempo_execucao int, 
    status_operacao varchar(20) not null, 
    quantidade_registros int, 
    foreign key (id_user) references users(id_user)
);

create table logs_errors (
    id_error INT PRIMARY KEY, 
    id_user INT, 
    data_error datetime, 
    msg_error varchar(50), 
    severidade varchar(100), 
    foreign key (id_user) references users(id_user)
);

/* Insert USERS */
INSERT INTO users VALUES
(1,'Carlos Silva','Financeiro','Administrador','Ativo'),
(2,'Fernanda Lima','RH','Analista','Ativo'),
(3,'João Pedro','TI','DBA','Ativo'),
(4,'Mariana Costa','Comercial','Usuário','Inativo'),
(5,'Ricardo Alves','TI','Administrador','Ativo'),
(6,'Amanda Souza','Financeiro','Analista','Ativo'),
(7,'Bruno Martins','RH','Usuário','Ativo'),
(8,'Patricia Gomes','Comercial','Gerente','Ativo'),
(9,'Lucas Pereira','TI','DBA','Ativo'),
(10,'Juliana Rocha','Financeiro','Usuário','Ativo'),
(11,'Felipe Santos','Marketing','Analista','Ativo'),
(12,'Camila Ribeiro','Marketing','Gerente','Ativo'),
(13,'Eduardo Lima','Comercial','Usuário','Ativo'),
(14,'Vanessa Almeida','TI','Analista','Ativo'),
(15,'Gabriel Mendes','RH','Administrador','Ativo'),
(16,'Renata Carvalho','Financeiro','Gerente','Ativo'),
(17,'Thiago Oliveira','TI','Usuário','Inativo'),
(18,'Larissa Fernandes','Comercial','Analista','Ativo'),
(19,'Rafael Costa','Marketing','Usuário','Ativo'),
(20,'Beatriz Nunes','RH','Gerente','Ativo');

/* Insert logs*/
INSERT INTO log_acess VALUES
(1,1,'2026-05-01 08:10:00','192.168.0.10','ERP','Sucesso'),
(2,2,'2026-05-01 08:15:00','192.168.0.11','RH','Sucesso'),
(3,3,'2026-05-01 08:20:00','192.168.0.12','Banco','Falha'),
(4,4,'2026-05-01 08:30:00','192.168.0.13','CRM','Sucesso'),
(5,5,'2026-05-01 08:45:00','192.168.0.14','ERP','Sucesso'),
(6,6,'2026-05-01 09:00:00','192.168.0.15','Financeiro','Falha'),
(7,7,'2026-05-01 09:10:00','192.168.0.16','RH','Sucesso'),
(8,8,'2026-05-01 09:20:00','192.168.0.17','CRM','Sucesso'),
(9,9,'2026-05-01 09:30:00','192.168.0.18','Banco','Sucesso'),
(10,10,'2026-05-01 09:40:00','192.168.0.19','ERP','Sucesso'),
(11,11,'2026-05-01 10:00:00','192.168.0.20','Marketing','Sucesso'),
(12,12,'2026-05-01 10:10:00','192.168.0.21','Marketing','Falha'),
(13,13,'2026-05-01 10:20:00','192.168.0.22','CRM','Sucesso'),
(14,14,'2026-05-01 10:30:00','192.168.0.23','Banco','Sucesso'),
(15,15,'2026-05-01 10:40:00','192.168.0.24','RH','Sucesso'),
(16,16,'2026-05-01 11:00:00','192.168.0.25','Financeiro','Sucesso'),
(17,17,'2026-05-01 11:10:00','192.168.0.26','ERP','Falha'),
(18,18,'2026-05-01 11:20:00','192.168.0.27','CRM','Sucesso'),
(19,19,'2026-05-01 11:30:00','192.168.0.28','Marketing','Sucesso'),
(20,20,'2026-05-01 11:40:00','192.168.0.29','RH','Sucesso');

INSERT INTO logs_operacoes VALUES
(1,1,'2026-05-01 08:30:00','UPDATE','clientes',250,'Sucesso',15),
(2,2,'2026-05-01 08:45:00','INSERT','funcionarios',300,'Sucesso',2),
(3,3,'2026-05-01 09:00:00','DELETE','pedidos',1200,'Lento',5),
(4,4,'2026-05-01 09:15:00','SELECT','vendas',180,'Sucesso',120),
(5,5,'2026-05-01 09:30:00','UPDATE','financeiro',600,'Sucesso',20),
(6,6,'2026-05-01 09:45:00','INSERT','clientes',450,'Sucesso',3),
(7,7,'2026-05-01 10:00:00','DELETE','usuarios',1500,'Lento',1),
(8,8,'2026-05-01 10:10:00','SELECT','produtos',200,'Sucesso',500),
(9,9,'2026-05-01 10:20:00','UPDATE','estoque',700,'Sucesso',30),
(10,10,'2026-05-01 10:30:00','INSERT','pedidos',350,'Sucesso',4),
(11,11,'2026-05-01 10:40:00','SELECT','campanhas',400,'Sucesso',250),
(12,12,'2026-05-01 10:50:00','UPDATE','marketing',1300,'Lento',12),
(13,13,'2026-05-01 11:00:00','SELECT','clientes',150,'Sucesso',600),
(14,14,'2026-05-01 11:10:00','DELETE','logs',1700,'Lento',50),
(15,15,'2026-05-01 11:20:00','UPDATE','usuarios',500,'Sucesso',8),
(16,16,'2026-05-01 11:30:00','SELECT','financeiro',900,'Sucesso',1000),
(17,17,'2026-05-01 11:40:00','INSERT','estoque',220,'Sucesso',6),
(18,18,'2026-05-01 11:50:00','UPDATE','pedidos',800,'Sucesso',18),
(19,19,'2026-05-01 12:00:00','SELECT','marketing',260,'Sucesso',700),
(20,20,'2026-05-01 12:10:00','DELETE','funcionarios',1400,'Lento',7);

INSERT INTO logs_errors VALUES
(1,1,'2026-05-01 08:35:00','Erro de conexão','Média'),
(2,2,'2026-05-01 08:50:00','Permissão negada','Alta'),
(3,3,'2026-05-01 09:05:00','Timeout na consulta','Alta'),
(4,4,'2026-05-01 09:20:00','Falha no SELECT','Baixa'),
(5,5,'2026-05-01 09:35:00','Erro de UPDATE','Média'),
(6,6,'2026-05-01 09:50:00','Chave duplicada','Média'),
(7,7,'2026-05-01 10:05:00','Deadlock encontrado','Alta'),
(8,8,'2026-05-01 10:15:00','Tabela inexistente','Baixa'),
(9,9,'2026-05-01 10:25:00','Erro de autenticação','Alta'),
(10,10,'2026-05-01 10:35:00','Falha de INSERT','Média'),
(11,11,'2026-05-01 10:45:00','Erro de índice','Baixa'),
(12,12,'2026-05-01 10:55:00','Timeout API','Alta'),
(13,13,'2026-05-01 11:05:00','Erro de permissão','Média'),
(14,14,'2026-05-01 11:15:00','Falha no DELETE','Alta'),
(15,15,'2026-05-01 11:25:00','Erro de trigger','Baixa'),
(16,16,'2026-05-01 11:35:00','Consulta muito lenta','Alta'),
(17,17,'2026-05-01 11:45:00','Erro de replicação','Alta'),
(18,18,'2026-05-01 11:55:00','Conexão perdida','Média'),
(19,19,'2026-05-01 12:05:00','Erro de encoding','Baixa'),
(20,20,'2026-05-01 12:15:00','Falha geral no sistema','Crítica');