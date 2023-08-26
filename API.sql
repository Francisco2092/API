Create database API;

Use API;
-- Crear tabla
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    edad INT,
    email VARCHAR(100)
);

-- INSERT - Agregar un nuevo usuario
INSERT INTO usuarios (nombre, edad, email) VALUES ('Usuario 1', 25, 'usuario1@example.com');

-- SELECT - Obtener todos los usuarios
SELECT * FROM usuarios;

-- UPDATE - Actualizar información de un usuario
UPDATE usuarios SET edad = 26 WHERE id = 1;

-- DELETE - Eliminar un usuario
DELETE FROM usuarios WHERE id = 1;
