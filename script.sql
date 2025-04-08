CREATE USER 'user_ptyhon'@'localhost' IDENTIFIED BY 'Clas3s1Nt2024_!';
GRANT CREATE, INSERT, UPDATE, DELETE, SELECT, FILE, EXECUTE ON *.* TO 'user_ptyhon'@'localhost' WITH GRANT OPTION;

CREATE DATABASE db_personas;

CREATE TABLE `db_personas`.`estados` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY(`id`)
);

CREATE TABLE `db_personas`.`personas` (
	`id` INT NOT NULL AUTO_INCREMENT,
    `cedula` VARCHAR(20) NOT NULL UNIQUE,
    `nombre` VARCHAR(250) NOT NULL,
    `estado` INT NOT NULL,
    `fecha` DATETIME NOT NULL,
    `activo` BIT NOT NULL,
    PRIMARY KEY(`id`),
    CONSTRAINT `fk_personas__estados` FOREIGN KEY (`estado`) REFERENCES `estados`(`id`)
);

INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Casad@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Solter@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Vioud@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Separados@s');
INSERT INTO `db_personas`.`estados` (`nombre`) VALUES ('Lo que importa es que Diosito me quiere');

INSERT INTO `db_personas`.`personas` (`cedula`,`nombre`,`estado`,`fecha`,`activo`) 
VALUES ('87987497','Pepito Perez',1,NOW(),1);
INSERT INTO `db_personas`.`personas` (`cedula`,`nombre`,`estado`,`fecha`,`activo`) 
VALUES ('12354646','Susana Lopez',2,NOW(),0);

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_select_estados`()
BEGIN
    SELECT `id`,
        `nombre`
    FROM `db_personas`.`estados`;
END$$

DELIMITER $$
CREATE PROCEDURE `db_personas`.`proc_insert_estados`(
    IN `Nombre` VARCHAR(50),
    INOUT `Respuesta` INT
)
BEGIN
    INSERT INTO `db_personas`.`estados` (`nombre`) 
    VALUES (`Nombre`);

    SET `Respuesta` = 0;
END$$
