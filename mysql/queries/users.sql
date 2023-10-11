
-- CREANDO USUARIOS
INSERT INTO users
(`id`,`first_name`,`last_name`,`email`,`created_at`,`update_at`)
VALUES
(1,"Coding","Dojo","Coding@dojo.cl",now(),now()),
(2,"alan","brito","alan@brito.cl",now(),now()),
(3,"elba","lazo","elba@lazo.cl",now(),now());

-- RECUPERANDO TODOS LOS DATOS
select *
from users;

-- RECUPERANDO EL PRIMER USUARIO QUE OCUPA EL CORREO
select *
from users
where email is not null
limit 1;

-- recupera el ultimo ususario que usa su id

SELECT *
FROM users
WHERE id IS NOT NULL
ORDER BY id DESC
LIMIT 1;

--  Cambia el usuario con id=3 para que su apellido sea Panqueques

UPDATE `asignaciones`.`users`
SET
`last_name` ='panqueques'
WHERE `id` = 2;


--  Elimina el usuario con id=2 de la base de datos

DELETE FROM `asignaciones`.`users`
WHERE id =2 ;

-- Obtén todos los usuarios, ordenados por su nombre

SELECT *
FROM users
ORDER BY first_name;

-- BONUS: obtén todos los usuarios, ordenados por su nombre en orden descendente

select * 
from users
ORDER BY first_name desc;
