CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_nutricional;

-- Tabla que contiene la información general de cada alimento
CREATE TABLE alimentos (
    id_alimento INT PRIMARY KEY AUTO_INCREMENT,
    nombre_comun VARCHAR(255) NOT NULL UNIQUE,
    nombre_cientifico VARCHAR(255),
    descripcion TEXT,
    tamano_porcion DECIMAL(10, 2),
    unidad_porcion VARCHAR(50) DEFAULT 'gramo'
    -- Se pueden agregar más campos generales sobre el alimento si es necesario
);

-- Tabla que contiene la lista de todos los nutrientes
CREATE TABLE nutrientes (
    id_nutriente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_nutriente VARCHAR(100) NOT NULL UNIQUE,
    unidad_medida VARCHAR(20) NOT NULL
);

-- Tabla que relaciona los alimentos con sus nutrientes y la cantidad por porción
CREATE TABLE composicion_nutricional (
    id_composicion INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_nutriente INT NOT NULL,
    cantidad DECIMAL(10, 3) NOT NULL,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_nutriente) REFERENCES nutrientes(id_nutriente),
    UNIQUE KEY `unica_composicion` (`id_alimento`, `id_nutriente`)
);

-- Tabla para relacionar alimentos con sus fuentes de datos nutricionales
CREATE TABLE alimentos_fuentes (
    id_alimento_fuente INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_fuente INT NOT NULL,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_fuente) REFERENCES fuentes_datos(id_fuente),
    UNIQUE KEY `unica_alimento_fuente` (`id_alimento`, `id_fuente`)
);