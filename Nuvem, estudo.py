 iaas = infraestrutura como serviço.
 definição = IaaS (Infraestrutura como Serviço) é um modelo de computação em nuvem onde provedores 
 terce tópicos sobre computação em nuvem:
irizados fornecem recursos fundamentais de TI — como servidores virtuais, armazenamento e redes
 sob demanda e via internet. A principal vantagem é o pagamento conforme
 o uso, o que elimina a necessidade de comprar e manter data centers físicos.
   (data centers) um lugar, infraestrutura bem organizada para armazenar processos envolvendo trabalho
 de grande escala,e de continuo. podendo ser em locais físicos ou em nuvem.

 A espinha dorsal de um data center é a redundância.
 Para garantir que serviços online, aplicativos e sites funcionem 24 horas por dia, 365 dias por ano,
 essas instalações possuem.

    Principais modos de uso.
 Corporativos: Estruturas próprias, montadas exclusivamente para atender as necessidades de uma única grande empresa.

   (SGBD) significa Sistema Gerenciador de Banco de Dados. É o software responsável por criar, organizar,
 manipular e proteger bancos de dados. Ele funciona como uma ponte segura entre a sua aplicação e os dados armazenados,  
garantindo a integridade e a consistência das informaçõe





use projeto;
CREATE TABLE funcionarios(
  id_funcionarios INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  idade VARCHAR(80) NOT NULL,
  email VARCHAR(150) UNIQUE,
  cpf CHAR(11),
  data_cadastro DATE
);

INSERT INTO funcionarios(id_funcionarios,nome, idade, email, cpf, data_cadastro)
VALUES (001,'Julia andrade', '24', 'jandrade@gmail.com','15477896534','2025-07-21');

INSERT INTO funcionarios(id_funcionarios,nome, idade, email, cpf, data_cadastro)
VALUES (002,'lucas da silva ', '19', 'lucassls@gmail.com','18745236958','2026-03-10'),
	   (003,'pedro henrique', '23', 'pedroh@gmail.com','54872365981','2023-05-28');
       


CREATE TABLE serviços (
  id_serviços INT AUTO_INCREMENT PRIMARY KEY,
  cargo VARCHAR(100) NOT NULL,
  modalidade VARCHAR(100) UNIQUE,
  salario DECIMAL(10,02),
  id_funcionarios INT,
  CONSTRAINT fk_serviços_funcionarios FOREIGN KEY (id_funcionarios)
  REFERENCES funcionarios (id_funcionarios)
);
  select * from serviços;
    INSERT INTO serviços(id_serviços, cargo,modalidade, salario,id_funcionarios)
    VALUES(001,'atendente',100,001);
    
    INSERT INTO serviços(id_serviços, cargo,modalidade, salario,id_funcionarios)
    VALUES(002,'atendente', 400, 002);
    
    INSERT INTO serviços(id_serviços,cargo, modalidade,salario, id_funcionarios)
    VALUES(003, 'instrutor de salao', 'academia',600,003);
       -------------------------------------------------
       continue...
use projeto;
CREATE TABLE funcionarios(
  id_funcionarios INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  idade VARCHAR(80) NOT NULL,
  email VARCHAR(150) UNIQUE,
  cpf CHAR(11),
  data_cadastro DATE
);
select * from funcionarios,serviços;
INSERT INTO funcionarios(id_funcionarios,nome, idade, email, cpf, data_cadastro)
VALUES (001,'Julia andrade', '24', 'jandrade@gmail.com','15477896534','2025-07-21');

INSERT INTO funcionarios(id_funcionarios,nome, idade, email, cpf, data_cadastro)
VALUES (002,'lucas da silva ', '19', 'lucassls@gmail.com','18745236958','2026-03-10'),
	   (003,'pedro henrique', '23', 'pedroh@gmail.com','54872365981','2023-05-28');
       


CREATE TABLE serviços (
  id_serviços INT AUTO_INCREMENT PRIMARY KEY,
  cargo VARCHAR(100) NOT NULL,
  modalidade VARCHAR(100) UNIQUE,
  salario DECIMAL(10,02),
  id_funcionarios INT,
  CONSTRAINT fk_serviços_funcionarios FOREIGN KEY (id_funcionarios)
  REFERENCES funcionarios (id_funcionarios)
);
  select * from funcionarios,serviços;
    INSERT INTO serviços(id_serviços, cargo,modalidade, salario,id_funcionarios)
    VALUES(001,'atendente',100,001);
    
    INSERT INTO serviços(id_serviços, cargo,modalidade, salario,id_funcionarios)
    VALUES(002,'atendente', 400, 002);
    
    INSERT INTO serviços(id_serviços,cargo, modalidade,salario, id_funcionarios)
    VALUES(003, 'instrutor de salao', 'academia',600,003);
            
            
            
 CREATE TABLE alunos(
   id_alunos INT AUTO_INCREMENT PRIMARY KEY,
   nome VARCHAR(100) NOT NULL,
   idade VARCHAR(80) NOT NULL,
   email VARCHAR(150) UNIQUE,
   cpf CHAR(11),
   data_cadastro DATE,
   id_serviços INT,
   CONSTRAINT fk_alunos_serviços FOREIGN KEY (id_serviços)
   REFERENCES serviços (id_serviços)
);

INSERT INTO alunos(id_alunos, nome, idade, email, cpf, data_cadastro)
VALUES (001,'alex pereiera', 27,'alex@yahoo.com','45789621354','2020-03-19');

select * from alunos,serviços;

select * from funcionarios a
inner join serviços b
on a.id_funcionarios = b.id_serviços;

          
