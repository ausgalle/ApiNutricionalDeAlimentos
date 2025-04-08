CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_nutricional;

--- Tabla que contiene la información general de cada alimento
CREATE TABLE alimentos (
    id_alimento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_comun VARCHAR(255) NOT NULL UNIQUE,
    nombre_cientifico VARCHAR(255),
    descripcion TEXT,
    tamano_porcion DECIMAL(10, 2),
    unidad_porcion VARCHAR(50) DEFAULT 'gramo',
    imagen_url VARCHAR(255),
    notas TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla que contiene la información general de cada alimento
CREATE TABLE alimentos (
    id_alimento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_comun VARCHAR(255) NOT NULL UNIQUE,
    nombre_cientifico VARCHAR(255),
    descripcion TEXT,
    tamano_porcion DECIMAL(10, 2),
    unidad_porcion VARCHAR(50) DEFAULT 'gramo',
    imagen_url VARCHAR(255),
    notas TEXT,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla que relaciona los alimentos con sus nutrientes y la cantidad por porción
CREATE TABLE composicion_nutricional (
    id_composicion INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_nutriente INT NOT NULL,
    cantidad DECIMAL(10, 5) NOT NULL,
    valor_diario_porcentaje DECIMAL(5, 2),
    notas TEXT,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_nutriente) REFERENCES nutrientes(id_nutriente),
    UNIQUE KEY `unica_composicion` (`id_alimento`, `id_nutriente`)
);

-- Tabla para clasificar los alimentos en diferentes categorías
CREATE TABLE categorias_alimentos (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);