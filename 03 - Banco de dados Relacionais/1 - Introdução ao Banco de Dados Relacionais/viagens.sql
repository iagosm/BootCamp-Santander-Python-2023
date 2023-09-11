CREATE TABLE usuarios(
	  id INT,
    nome VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    endereco VARCHAR(50) NOT NULL,
    data_nascimento DATE NOT NULL
);

CREATE TABLE destinos(
	id int,
    nome VARCHAR(255) NOT NULL UNIQUE,
    descricao VARCHAR(255) NOT NULL
);

CREATE TABLE reservas (
  id INT,
  id_usuario INT,
  id_destino INT,
  data DATE,
  status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada e etc)' 
);

INSERT INTO usuarios (id, nome, email, data_nascimento, endereco) VALUES
 (1, "Iago", "teste@gmail.com", "2000-06-30", "Endereço qualquer para teste");

 INSERT INTO destinos (id, nome, descricao) VALUES (1, "Praia do Rosa", "Linda Praia");

 INSERT INTO reservas (id, id_usuario, id_destino, status, data) VALUES (1, 1, 1, 'pendente', '2023-11-11');