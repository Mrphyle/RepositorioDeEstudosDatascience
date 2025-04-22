CREATE TABLE Nota_Fiscal (
    id_cliente INT PRIMARY KEY NOT NULL,
    razao_social VARCHAR(50),
    cnpj_cpf VARCHAR(14),
    inscricao_estadual VARCHAR(12),
    endereco VARCHAR(50),
    id_cep VARCHAR(8),
    fone_fax VARCHAR(15),
    id_produto VARCHAR(50),
    qtde DECIMAL(10,2),
    preco_total DECIMAL(10,2),
    desconto DECIMAL(10,2),
    bcip DECIMAL(10,2),
    vrl_icms DECIMAL(10,2),
    vrl_ipi DECIMAL(10,2),
    icms_percent DECIMAL(5,2),
    ipi_percent DECIMAL(5,2)
);
CREATE TABLE Cliente (
    id_cliente INT,
    razao_social VARCHAR(50),
    cnpj_cpf VARCHAR(14),
    inscricao_estadual VARCHAR(12),
    endereco VARCHAR(50),
    id_cep VARCHAR(8),
    fone_fax VARCHAR(15),
);
CREATE TABLE cep (
    id_cep INT,
    Cidade VARCHAR(50),
    logradouro VARCHAR(50),
    bairro VARCHAR(75),
    uf VARCHAR(2)
);
CREATE TABLE produto (
    id_produto INT,
    descricao_produto_servico VARCHAR(50),
    qtde int,
    preco_un int,
    ncm_sh VARCHAR(8),
    csosn VARCHAR(2),
    cfop VARCHAR(4),
);