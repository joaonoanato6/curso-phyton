use teste_sql;

CREATE TABLE funcinarios(
  id_funcionarios INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  idade VARCHAR(80) NOT NULL,
  email VARCHAR(150) UNIQUE,
  cpf CHAR(11),
  numero_contato VARCHAR(11) UNIQUE,
  data_cadastro DATE,
  cargo_funcionario VARCHAR(80)
);
  INSERT INTO funcinarios(id_funcionarios,nome, idade, email, data_cadastro, cargo_funcionario)
  VALUES (001,'Julia andrade', '24', 'jandrade@gmail.com','2025-07-21', 'atendente');
  
  INSERT INTO 	funcinarios(id_funcionarios,nome, idade,email,data_cadastro,cargo_funcionario)
  VALUES  (002,'lucas da silva ', '19', 'lucassls@gmail.com','2026-03-10', 'instrutor de salao'),
          (003,'pedro henrique', '23', 'pedroh@gmail.com','2023-05-28', 'instrutor de salao'),
          (004,'alice almeida', '22', 'alicai@hotmail.com','2023-02-18', 'atendente');
  
  SELECT * FROM funcinarios;


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
          
          
