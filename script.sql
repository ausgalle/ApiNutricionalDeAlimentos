CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_nutricional;

--- Tabla 1 que contiene la información general de cada alimento
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

-- Tabla 2 que contiene la información general de cada alimento
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

-- Tabla 3 que relaciona los alimentos con sus nutrientes y la cantidad por porción
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

-- Tabla 4 para clasificar los alimentos en diferentes categorías
CREATE TABLE categorias_alimentos (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla 5 para relacionar alimentos con sus categorías
CREATE TABLE alimentos_categorias (
    id_alimento_categoria INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_categoria) REFERENCES categorias_alimentos(id_categoria),
    UNIQUE KEY `unica_alimento_categoria` (`id_alimento`, `id_categoria`)
);

-- Tabla 6 para rastrear la fuente de los datos nutricionales
CREATE TABLE fuentes_datos (
    id_fuente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_fuente VARCHAR(255) NOT NULL UNIQUE,
    descripcion_fuente TEXT,
    url_fuente VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla 7 para relacionar alimentos con sus fuentes de datos nutricionales
CREATE TABLE alimentos_fuentes (
    id_alimento_fuente INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_fuente INT NOT NULL,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    notas TEXT,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_fuente) REFERENCES fuentes_datos(id_fuente),
    UNIQUE KEY `unica_alimento_fuente` (`id_alimento`, `id_fuente`)
);

-- Tabla 8 para almacenar las diferentes unidades de medida utilizadas
CREATE TABLE unidades_medida (
    id_unidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_unidad VARCHAR(50) NOT NULL UNIQUE,
    simbolo VARCHAR(10) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla 9 para relacionar nutrientes con sus unidades de medida comunes (si es necesario)
CREATE TABLE nutrientes_unidades (
    id_nutriente_unidad INT PRIMARY KEY AUTO_INCREMENT,
    id_nutriente INT NOT NULL,
    id_unidad INT NOT NULL,
    es_default BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_nutriente) REFERENCES nutrientes(id_nutriente),
    FOREIGN KEY (id_unidad) REFERENCES unidades_medida(id_unidad),
    UNIQUE KEY `unica_nutriente_unidad` (`id_nutriente`, `id_unidad`)
);

-- Tabla 10 para definir etiquetas nutricionales
CREATE TABLE etiquetas_nutricionales (
    id_etiqueta INT PRIMARY KEY AUTO_INCREMENT,
    nombre_etiqueta VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla 11 para relacionar alimentos con sus etiquetas nutricionales
CREATE TABLE alimentos_etiquetas (
    id_alimento_etiqueta INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_etiqueta INT NOT NULL,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_etiqueta) REFERENCES etiquetas_nutricionales(id_etiqueta),
    UNIQUE KEY `unica_alimento_etiqueta` (`id_alimento`, `id_etiqueta`)
);

-- Tabla 12 para almacenar información sobre alérgenos
CREATE TABLE alergenos (
    id_alergeno INT PRIMARY KEY AUTO_INCREMENT,
    nombre_alergeno VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla 13 para relacionar alimentos con los alérgenos que contienen
CREATE TABLE alimentos_alergenos (
    id_alimento_alergeno INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_alergeno INT NOT NULL,
    contiene BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_alergeno) REFERENCES alergenos(id_alergeno),
    UNIQUE KEY `unica_alimento_alergeno` (`id_alimento`, `id_alergeno`)
);

-- Tabla 14 para almacenar información de usuarios de la API (si es necesario)
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultimo_login TIMESTAMP
);
