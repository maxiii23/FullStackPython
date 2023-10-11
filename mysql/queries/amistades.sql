-- Consulta: crea 6 usuarios nuevos
INSERT INTO mydb.users (first_name, last_name) VALUES
('Amy', 'Giver'),
('Eli', 'Byers'),
('Marky', 'Mark'),
('benjamin', 'herrera'),
('juan', 'perez'),
('pedro', 'guitierrez');

-- Consulta: haz que el usuario 2 sea amigo del usuario 1, 3 y 5

INSERT INTO friendships (users_id, friend_id1) VALUES
(1, 2),
(1, 4),  
(1, 6);

-- Consulta: haz que el usuario 2 sea amigo del usuario 1, 3 y 5

INSERT INTO friendships (users_id, friend_id1) VALUES
(2, 1),
(2, 3),  
(2, 5);

-- Consulta: haz que el usuario 3 sea amigo del usuario 2 y 5
INSERT INTO friendships (users_id, friend_id1) VALUES
(3, 2),
(3, 5);

-- Consulta: haz que el usuario 4 sea amigo del usuario 3
INSERT INTO friendships (users_id, friend_id1) VALUES
(4, 3);

-- Consulta: haz que el usuario 5 sea amigo del usuario 1 y 6

INSERT INTO friendships (users_id, friend_id1) VALUES
(5, 1),
(5, 6);

-- Consulta: haz que el usuario 6 sea amigo del usuario 2 y 3

INSERT INTO friendships (users_id, friend_id1) VALUES
(6, 2),
(6, 3);

-- Consulta: muestra las relaciones creadas

SELECT *
FROM `mydb`.`friendships`;

--  Devuelve todos los usuarios que son amigos del primer usuario.

SELECT
    u2.first_name AS 'nombre del amigo',
    u2.last_name AS 'apellido del amigo'
FROM
    mydb.friendships AS f
INNER JOIN
    mydb.users AS u1 ON f.users_id = u1.id
INNER JOIN
    mydb.users AS u2 ON f.friend_id1 = u2.id
WHERE
    u1.first_name = 'Amy' AND u1.last_name = 'Giver';

-- Consulta NINJA: Devuelve el recuento de todas las amistades

SELECT
    u1.first_name AS 'nombre de usuario',
    u1.last_name AS 'apellido de usuario',
    u2.first_name AS 'nombre de amigo',
    u2.last_name AS 'apellido de amigo'
FROM
    mydb.friendships AS f
INNER JOIN
    mydb.users AS u1 ON f.users_id = u1.id
INNER JOIN
    mydb.users AS u2 ON f.friend_id1 = u2.id;

-- Consulta NINJA: averigua quién tiene más amigos y devuelve la cuenta de sus amigos.

SELECT
    u1.first_name AS nombre,
    u1.last_name AS apellido,
    COUNT(f.id) AS 'total de amigos'
FROM
    mydb.users AS u1
LEFT JOIN
    mydb.friendships AS f ON u1.id = f.users_id
GROUP BY
    u1.id
ORDER BY
    'total de amigos' DESC
LIMIT 1;

-- Consulta NINJA: Devuelve los amigos del tercer usuario en orden alfabético

SELECT
    u.first_name AS friend_first_name,
    u.last_name AS friend_last_name
FROM
    mydb.friendships AS f
INNER JOIN
    mydb.users AS u ON f.friend_id1 = u.id
WHERE
    f.users_id = 3 
ORDER BY
    u.first_name ASC, u.last_name ASC;