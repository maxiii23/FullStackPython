-- Consulta: crea 5 usuarios diferentes
INSERT INTO `asignaciones`.`usuarios`
(`id`,
`first_name`,
`last_name`,
`created_at`,
`update_at`)
VALUES
(1,"Jane","Austen",now(),now()),
(2,"Emily","Dickinson",now(),now()),  
(3,"Fyodor","Dostoevsky",now(),now()),
(4,"William","Shakespeare",now(),now()),
(5,"Lau","Tzu",now(),now());

-- Consulta: crea 5 libros

INSERT INTO `asignaciones`.`books`
(`id`,
`title`,
`num_of_pages`,
`created_at`,
`updated_at`)
VALUES
(1,"C sHARP",1111,now(),now()),
(2,"C Java",1111,now(),now()),
(3,"Python",1111,now(),now()),
(4,"PHP",1111,now(),now()),
(5,"Ruby",1111,now(),now());

-- cambiar el nombre de el libro "c Sharp"

UPDATE `asignaciones`.`books`
SET
`title` = "C#"
WHERE id = 1;

-- Consulta: cambia el nombre del cuarto usuario a Bill

UPDATE `asignaciones`.`usuarios`
SET `first_name` = "Bill"
WHERE id = 4;

-- Consulta: haz que el primer usuario marque como favorito los 2 primeros libros

INSERT INTO `asignaciones`.`favorites`
(`user_id`,`book_id`)
VALUES
(1,1),
(1,2);
  
-- Consulta: haz que el segundo usuario marque como favorito los primeros 3 libros
  
INSERT INTO `asignaciones`.`favorites`
(`user_id`, `book_id`)
VALUES
(2, 1),
(2, 2),
(2, 3);

-- Consulta: haz que el tercer usuario marque como favorito los 4 primeros libros

INSERT INTO `asignaciones`.`favorites`
(`user_id`, `book_id`)
VALUES
(3, 1),
(3, 2),
(3, 3),
(3, 4);


select * 
from favorites

-- Consulta: Haz que el cuarto usuario marque como favorito todos los libros

INSERT INTO `asignaciones`.`favorites`
(`user_id`, `book_id`)
VALUES
(4, 1),
(4, 2),
(4, 3),
(4, 4),
(4, 5);

-- Consulta: recupera todos los usuarios que marcaron como favorito el tercer libro

SELECT u.*
FROM asignaciones.usuarios u
INNER JOIN asignaciones.favorites f ON u.id = f.user_id
WHERE f.book_id = 3;

-- Consulta: elimina el primer usuario de los favoritos del tercer libro

DELETE FROM asignaciones.favorites
WHERE user_id = (SELECT id FROM asignaciones.usuarios ORDER BY id ASC LIMIT 1)
AND book_id = 3;

-- Consulta: Haz que el quinto usuario marque como favorito el segundo libro

INSERT INTO `asignaciones`.`favorites`
(`user_id`, `book_id`)
VALUES
(5, 2);

-- Encuentra todos los libros que el tercer usuario marcó como favoritos

SELECT b.*
FROM asignaciones.books b
INNER JOIN asignaciones.favorites f ON b.id = f.book_id
WHERE f.user_id = 3;

-- Consulta: encuentra todos los usuarios que marcaron como favorito el quinto libro

SELECT u.*
FROM asignaciones.usuarios u
INNER JOIN asignaciones.favorites f ON u.id = f.user_id
WHERE f.book_id = 5;