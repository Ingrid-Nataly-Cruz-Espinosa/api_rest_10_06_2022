clientes.sql
DROP TABLE IF EXISTS clientes;

CREATE TABLE clientes(
    id_cliente integer PRIMARY KEY AUTOINCREMENT,
    nombre varchar(50) NOT NULL,
    email varchar(50) NOT NULL
);

INSERT INTO clientes(nombre, email) VALUES('Dejah','deja@email.com');
INSERT INTO clientes(nombre, email) VALUES('John','john@email.com');
INSERT INTO clientes(nombre, email) VALUES('Carthoris','carthotis@email.com');

.headers ON

SELECT * FROM clientes;