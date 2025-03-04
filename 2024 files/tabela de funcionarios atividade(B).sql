--1:
CREATE TABLE func(id int  PRIMARY KEY AUTO_INCREMENT, full_name varchar(100),sex varchar(1),date_of_birth varchar(10),hiring_date varchar(10), base_salary int, nivel varchar(70), area varchar(70))
--2:
INSERT INTO func(full_name,sex,date_of_birth,hiring_date,base_salary,nivel,area) VALUES ("Adelino Araujo","M","04/09/1976","07/11/2005",853,"Estagiario","Operacoes")
--3:
SELECT * FROM func GROUP BY full_name
--4:
SELECT AVG(base_salary) FROM func 
--5:
SELECT AVG(date_of_birth) FROM func
--6:
SELECT COUNT(*) FROM func WHERE sex="F"
--7:
SELECT COUNT(*) FROM func WHERE area="Administrativo"
--8:
SELECT hiring_date FROM func
--9:
SELECT DISTINCT(area),COUNT(*) FROM func GROUP BY area
--10:
SELECT * FROM func BETWEEN date_of_birth="01/01/1985" AND date_of_birth="13/09/2024"
--Ignore a linha 22 prof, coloquei só para eu ver como era o certo da pergunta 10:
SELECT * FROM func WHERE date_of_birth BETWEEN '01/01/1985' AND '13/09/2024'