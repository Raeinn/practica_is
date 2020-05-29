DROP DATABASE IF EXISTS si_cine;
CREATE DATABASE si_cine;
USE si_cine;

# Parent tables
CREATE TABLE IF NOT EXISTS usuarios (
    u_id VARCHAR(12) NOT NULL,
    u_password VARCHAR(12) NOT NULL,
    is_admin BOOL NOT NULL,
    PRIMARY KEY (u_id)
);

CREATE TABLE IF NOT EXISTS peliculas (
    p_id INT NOT NULL AUTO_INCREMENT,
    nombre VARCHAR(60) NOT NULL,
    genero VARCHAR(20) NOT NULL,
    clasificacion VARCHAR(5) NOT NULL,
    PRIMARY KEY (p_id)
);

CREATE TABLE IF NOT EXISTS salas (
    s_id CHAR NOT NULL,
    descripcion VARCHAR(12) NOT NULL,
    PRIMARY KEY (s_id)
);

# Child tables
CREATE TABLE IF NOT EXISTS asientos (
    a_id VARCHAR(4) NOT NULL,
    sala CHAR NOT NULL,
    PRIMARY KEY (a_id),
    FOREIGN KEY (sala) REFERENCES salas(s_id)
);

CREATE TABLE IF NOT EXISTS funciones (
    f_id INT NOT NULL AUTO_INCREMENT,
    pelicula INT NOT NULL,
    sala CHAR NOT NULL,
    fecha_emision DATETIME NOT NULL,
    PRIMARY KEY (f_id),
    CONSTRAINT FK_Funcion_Pelicula
        FOREIGN KEY (pelicula) REFERENCES peliculas(p_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (sala) REFERENCES salas(s_id),
    CONSTRAINT UQ_Funcion UNIQUE (sala, fecha_emision)
);

CREATE TABLE IF NOT EXISTS boletos (
    b_id INT NOT NULL AUTO_INCREMENT,
    funcion INT NOT NULL,
    asiento VARCHAR(4) NOT NULL,
    PRIMARY KEY (b_id),
    FOREIGN KEY (funcion) REFERENCES funciones(f_id),
    FOREIGN KEY (asiento) REFERENCES asientos(a_id)
);

CREATE TABLE IF NOT EXISTS boletos_usuarios (
    boleto INT NOT NULL,
    usuario VARCHAR(12) NOT NULL,
    CONSTRAINT PK_Boleto_Usuario PRIMARY KEY (boleto, usuario),
    FOREIGN KEY (boleto) REFERENCES boletos(b_id),
    FOREIGN KEY (usuario) REFERENCES usuarios(u_id)
);

INSERT INTO usuarios(u_id, u_password, is_admin) VALUES('Iarklan', 'TestCod3', 1);
INSERT INTO peliculas(nombre, genero, clasificacion) VALUES('Testing', 'Comedia', 'A');
INSERT INTO salas(s_id, descripcion) VALUES('A', 'Sala A');
# SELECT u_id, is_admin FROM usuarios;
# Rin, shiro