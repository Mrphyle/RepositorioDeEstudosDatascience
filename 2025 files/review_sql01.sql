create database DbLibrary

create table book(id int primary key, title varchar(200) not null,autor varchar(500) not null, editora varchar(50) not null, edicao int not null, genero varchar(100) not null)

insert into book(id,title,autor,editora,edicao,genero) values (9788539629589,Exel 2019,Senac são Paulo,01,informatica)

Select * From book
