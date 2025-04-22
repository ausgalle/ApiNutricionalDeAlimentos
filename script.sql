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
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
);

-- Insertar datos de ejemplo en la tabla alimentos
INSERT INTO alimentos (nombre_comun, nombre_cientifico, descripcion, tamano_porcion, unidad_porcion, imagen_url, notas) VALUES
('Manzana', 'Malus domestica', 'Fruta dulce y crujiente.', 100.00, 'gramo', 'https://example.com/manzana.jpg', 'Consumir fresca.'),
('Banana', 'Musa acuminata', 'Fruta amarilla rica en potasio.', 100.00, 'gramo', 'https://example.com/banana.jpg', 'Ideal para batidos.'),
('Espinaca', 'Spinacia oleracea', 'Vegetal de hoja verde rico en hierro.', 100.00, 'gramo', 'https://example.com/espinaca.jpg', 'Consumir cocida o cruda.'); 

-- Tabla 3
CREATE TABLE nutrientes (
    id_nutriente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_nutriente VARCHAR(100) NOT NULL UNIQUE,
    unidad_medida VARCHAR(20) NOT NULL
);

-- Tabla 4 que relaciona los alimentos con sus nutrientes y la cantidad por porción
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

-- Tabla 5 para clasificar los alimentos en diferentes categorías
CREATE TABLE categorias_alimentos (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla 6 para relacionar alimentos con sus categorías
CREATE TABLE alimentos_categorias (
    id_alimento_categoria INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_categoria INT NOT NULL,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_categoria) REFERENCES categorias_alimentos(id_categoria),
    UNIQUE KEY `unica_alimento_categoria` (`id_alimento`, `id_categoria`)
);

-- Tabla 7 para rastrear la fuente de los datos nutricionales
CREATE TABLE fuentes_datos (
    id_fuente INT PRIMARY KEY AUTO_INCREMENT,
    nombre_fuente VARCHAR(255) NOT NULL UNIQUE,
    descripcion_fuente TEXT,
    url_fuente VARCHAR(255),
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla 8 para relacionar alimentos con sus fuentes de datos nutricionales
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

-- Tabla 9 para almacenar las diferentes unidades de medida utilizadas
CREATE TABLE unidades_medida (
    id_unidad INT PRIMARY KEY AUTO_INCREMENT,
    nombre_unidad VARCHAR(50) NOT NULL UNIQUE,
    simbolo VARCHAR(10) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla 10 para relacionar nutrientes con sus unidades de medida comunes (si es necesario)
CREATE TABLE nutrientes_unidades (
    id_nutriente_unidad INT PRIMARY KEY AUTO_INCREMENT,
    id_nutriente INT NOT NULL,
    id_unidad INT NOT NULL,
    es_default BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_nutriente) REFERENCES nutrientes(id_nutriente),
    FOREIGN KEY (id_unidad) REFERENCES unidades_medida(id_unidad),
    UNIQUE KEY `unica_nutriente_unidad` (`id_nutriente`, `id_unidad`)
);

-- Tabla 11 para definir etiquetas nutricionales
CREATE TABLE etiquetas_nutricionales (
    id_etiqueta INT PRIMARY KEY AUTO_INCREMENT,
    nombre_etiqueta VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);

-- Tabla 12 para relacionar alimentos con sus etiquetas nutricionales
CREATE TABLE alimentos_etiquetas (
    id_alimento_etiqueta INT PRIMARY KEY AUTO_INCREMENT,
    id_alimento INT NOT NULL,
    id_etiqueta INT NOT NULL,
    FOREIGN KEY (id_alimento) REFERENCES alimentos(id_alimento),
    FOREIGN KEY (id_etiqueta) REFERENCES etiquetas_nutricionales(id_etiqueta),
    UNIQUE KEY `unica_alimento_etiqueta` (`id_alimento`, `id_etiqueta`)
);

-- Tabla 13 para almacenar los roles de los usuarios
CREATE TABLE roles (
    id_rol INT PRIMARY KEY AUTO_INCREMENT,
    nombre_rol VARCHAR(50) NOT NULL UNIQUE,
    descripcion TEXT,
    fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion DATETIME ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla 14 para almacenar información de usuarios de la API (si es necesario)
-- Tabla para almacenar la información de los usuarios
CREATE TABLE usuarios (
    id_usuario INT PRIMARY KEY AUTO_INCREMENT,
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    contrasena VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE,
    id_rol INT DEFAULT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    ultimo_login DATETIME,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
);

-- Tabla 15 para almacenar los diferentes permisos del sistema
CREATE TABLE permisos (
    id_permiso INT PRIMARY KEY AUTO_INCREMENT,
    nombre_permiso VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT,
    nombre_corto VARCHAR(50) UNIQUE,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabla 16 para relacionar roles con los permisos que tienen asignados
CREATE TABLE roles_permisos (
    id_rol_permiso INT PRIMARY KEY AUTO_INCREMENT,
    id_rol INT NOT NULL,
    id_permiso INT NOT NULL,
    FOREIGN KEY (id_rol) REFERENCES roles(id_rol),
    FOREIGN KEY (id_permiso) REFERENCES permisos(id_permiso),
    UNIQUE KEY `unica_rol_permiso` (`id_rol`, `id_permiso`)
);

-- SCRIPTS DE PROCEDIMIENTOS DE ALMACENADO

-- Delimitador para poder definir el procedimiento almacenado completo
DELIMITER //
CREATE PROCEDURE proc_insert_alimento (
    IN p_nombre_comun VARCHAR(255),
    IN p_nombre_cientifico VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_tamano_porcion DECIMAL(10,5),
    IN p_unidad_porcion VARCHAR(50),
    IN p_imagen_url VARCHAR(255),
    IN p_notas TEXT,
    IN p_fecha_creacion DATETIME,
    IN p_fecha_actualizacion DATETIME
)
BEGIN
    INSERT INTO alimentos (
        nombre_comun,
        nombre_cientifico,
        descripcion,
        tamano_porcion,
        unidad_porcion,
        imagen_url,
        notas,
        fecha_creacion,
        fecha_actualizacion
    )
    VALUES (
        p_nombre_comun,
        p_nombre_cientifico,
        p_descripcion,
        p_tamano_porcion,
        p_unidad_porcion,
        p_imagen_url,
        p_notas,
        p_fecha_creacion,
        p_fecha_actualizacion
    );
END //
DELIMITER ;


DELIMITER $$

CREATE PROCEDURE proc_update_alimento(
    IN p_id_alimento INT,
    IN p_nombre_comun VARCHAR(255),
    IN p_nombre_cientifico VARCHAR(255),
    IN p_descripcion TEXT,
    IN p_tamano_porcion DECIMAL(10, 2),
    IN p_unidad_porcion VARCHAR(50),
    IN p_imagen_url VARCHAR(255),
    IN p_notas TEXT,
    IN p_fecha_actualizacion DATETIME,
    IN p_fecha_creacion DATETIME
)
BEGIN
    UPDATE alimentos
    SET
        nombre_comun = p_nombre_comun,
        nombre_cientifico = p_nombre_cientifico,
        descripcion = p_descripcion,
        tamano_porcion = p_tamano_porcion,
        unidad_porcion = p_unidad_porcion,
        imagen_url = p_imagen_url,
        notas = p_notas,
        fecha_actualizacion = p_fecha_actualizacion
    WHERE id_alimento = p_id_alimento;
END $$

DELIMITER ;


DELIMITER $$

CREATE PROCEDURE proc_delete_alimento(IN p_id_alimento INT)
BEGIN
    DELETE FROM alimentos
    WHERE id_alimento = p_id_alimento;
END $$

DELIMITER ;


DELIMITER //

CREATE PROCEDURE proc_insert_nutriente (
    IN p_nombre_nutriente VARCHAR(100),
    IN p_unidad_medida VARCHAR(20)
)
BEGIN
    INSERT INTO nutrientes (nombre_nutriente, unidad_medida)
    VALUES (p_nombre_nutriente, p_unidad_medida);
END //

DELIMITER ;