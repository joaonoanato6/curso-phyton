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
