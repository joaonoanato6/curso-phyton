    [psicanálise app]

1 fazer um sistema no qual insira os dados do cliente:
2 fazer uma escala de duração serviço contratado =
sendo hora / mês do contrato do mesmo:
3 montar uma estrutura de decisão na qual informe, sobre
os horário e os dias disponíveis.
4 montar um guia de contato do prestador de serviço para o 
contratante:
5 informa os planos de oferta para o contratante dos serviços
com o valor.

parte matemática
 
1 conversão de mês pra dia vice e versa.
2 soma, divisão.
3 conversão de hora para minuto /dia.




projeto banco de dados[´]
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
  
  SELECT * FROM funcionarios;
  

