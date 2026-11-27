USE academia;


CREATE TABLE setor (
    id_setor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255)
);
INSERT INTO setor (nome, descricao) VALUES
('Musculação', 'Setor de treinamento muscular'),
('Recepção', 'Atendimento aos alunos'),
('Administrativo', 'Gerenciamento da academia'),
('Ginástica', 'Aulas coletivas'),
('Manutenção', 'Manutenção dos equipamentos');

-- TABELA SERVICO
CREATE TABLE servico (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(255),
    valor DECIMAL(10,2)
);
INSERT INTO servico (nome, descricao, valor) VALUES
('Musculação', 'Treinamento com pesos e aparelhos', 120.00),
('Pilates', 'Exercícios de flexibilidade e postura', 150.00),
('Spinning', 'Aula de bicicleta indoor', 100.00),
('Zumba', 'Aula coletiva de dança', 90.00),
('Funcional', 'Treinamento funcional', 110.00);

-- TABELA FUNCIONARIO
CREATE TABLE funcionario (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE,
    telefone VARCHAR(20),
    cargo VARCHAR(100),
    salario DECIMAL(10,2),
    id_setor INT,
    FOREIGN KEY (id_setor)
        REFERENCES setor(id_setor)
);
INSERT INTO funcionario
(nome, cpf, telefone, cargo, salario, id_setor)
VALUES
('Carlos Silva', '141.951.871-11', '21999990001', 'Professor', 3000.00, 1),
('Ana Souza', '922.782.287-57', '21999990002', 'Recepcionista', 1800.00, 2),
('Pedro Santos', '333.333.333-33', '21999990003', 'Gerente', 4500.00, 3),
('Mariana Costa', '444.457.784-34', '21999990004', 'Instrutora', 2800.00, 4),
('Lucas Oliveira', '355.785.787-45', '21999990005', 'Técnico', 2500.00, 5),
('Fernanda Lima', '665.698.986-26', '21999990006', 'Professora', 3200.00, 1);

-- TABELA ALUNO
CREATE TABLE aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE,
    data_nascimento DATE,
    telefone VARCHAR(20),
    email VARCHAR(100),
    endereco VARCHAR(200),
    data_matricula DATE
);
INSERT INTO aluno
(nome, cpf, data_nascimento, telefone, email, endereco, data_matricula)
VALUES
('João Pereira', '344.774.877-77', '2000-05-10', '219888848751', 'joao@email.com', 'Rua A, 100', '2026-01-10'),
('Maria Almeida', '888.788.548-88', '1998-08-15', '21988880002', 'maria@email.com', 'Rua B, 200', '2026-01-12'),
('Rafael Mendes', '999.699.999-99', '2002-03-20', '21988880003', 'rafael@email.com', 'Rua C, 300', '2026-01-15'),
('Juliana Rocha', '123.456.789-10', '1995-11-25', '219889658004', 'juliana@email.com', 'Rua D, 400', '2026-01-18'),
('Bruno Ferreira', '234.567.890-12', '2001-07-05', '21985480095', 'bruno@email.com', 'Rua E, 500', '2026-01-20'),
('Camila Martins', '345.678.901-23', '1999-02-14', '21988887006', 'camila@email.com', 'Rua F, 600', '2026-01-22'),
('Gabriel Ribeiro', '456.789.012-34', '2003-09-30', '21988857807', 'gabriel@email.com', 'Rua G, 700', '2026-01-25'),
('Beatriz Gomes', '567.890.123-45', '1997-04-18', '21988848708', 'beatriz@email.com', 'Rua H, 800', '2026-01-28');

-- TABELA TURMA
CREATE TABLE turma (
    id_turma INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    horario TIME,
    dia_semana VARCHAR(20),
    capacidade INT,
    id_funcionario INT,
    id_servico INT,
    FOREIGN KEY (id_funcionario)
        REFERENCES funcionario(id_funcionario),
    FOREIGN KEY (id_servico)
        REFERENCES servico(id_servico)
);
INSERT INTO turma
(nome, horario, dia_semana, capacidade, id_funcionario, id_servico)
VALUES
('Musculação', 'Manhã', '08:00:00', 'Segunda', 20, 1, 1),
('Pilates','Tarde', '14:00:00', 'Terça', 15, 4, 2),
('Spinning', 'Noite', '19:00:00', 'Quarta', 20, 1, 3),
('Zumba','Manhã', '09:00:00', 'Quinta', 25, 4, 4),
('Funcional','Noite', '18:00:00', 'Sexta', 20, 6, 5),
('Musculação', 'Tarde', '16:00:00', 'Segunda', 20, 6, 1);

-- TABELA MAQUINARIO
CREATE TABLE maquinario (
    id_maquinario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    marca VARCHAR(100),
    quantidade INT,
    estado VARCHAR(50),
    id_setor INT,
    FOREIGN KEY (id_setor)
        REFERENCES setor(id_setor)
);
INSERT INTO maquinario
(nome, marca, quantidade, estado, id_setor)
VALUES
('Esteira', 'Movement', 10, 'Bom', 1),
('Bicicleta Ergométrica', 'Kikos', 8, 'Bom', 1),
('Leg Press', 'Movement', 4, 'Bom', 1),
('Supino Reto', 'Matrix', 5, 'Bom', 1),
('Halteres', 'LiveUp', 30, 'Bom', 1),
('Colchonetes', 'Acte', 20, 'Regular', 4),
('Bicicleta de Spinning', 'Schwinn', 12, 'Bom', 4),
('Equipamento de Pilates', 'Metalife', 5, 'Bom', 4);

-- TABELA MATRICULA_TURMA
CREATE TABLE matricula_turma (
    id_aluno INT,
    id_turma INT,
    data_matricula DATE,
    PRIMARY KEY (id_aluno, id_turma),
    FOREIGN KEY (id_aluno)
        REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_turma)
        REFERENCES turma(id_turma)
);
INSERT INTO matricula_turma
(id_aluno, id_turma, data_matricula)
VALUES
(1, 1, '2018-07-10'),
(2, 2, '2022-01-12'),
(3, 3, '2023-03-20'),
(4, 4, '2022-08-18'),
(5, 5, '2026-09-09'),
(6, 1, '2027-10-05'),
(7, 3, '2011-04-06');

SELECT * FROM servico;

SELECT * FROM setor;

SELECT * FROM turma;

SELECT * FROM aluno
WHERE nome = 'João Pereira';

SELECT * FROM aluno
WHERE nome = 'João Pereira';

SELECT * FROM funcionario
WHERE salario > 2500;

##consulta periodo cadastro##
SELECT * FROM aluno
WHERE MONTH(data_matricula) = 1
AND YEAR(data_matricula) = 2026;

SELECT
    f.nome AS funcionario,
    f.cargo,
    s.nome AS setor
FROM funcionario f
INNER JOIN setor s
    ON f.id_setor = s.id_setor;
