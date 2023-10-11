-- Consulta: crea 3 dojos nuevos

INSERT INTO `dojos`
(`id`,
`name`,
`created_at`,
`update_at`)
VALUES
(1,"coding dojo",now(),now()),
(2,"aml-sip",now(),now()),
(3,"sip-sanbernardo",now(),now());

-- Consulta: elimina los 3 dojos que acabas de crear

DELETE FROM `asignaciones`.`dojos`
WHERE id IN (1, 2, 3);

-- Consulta: crea 3 dojos nuevos

INSERT INTO `dojos`
(`id`,
`name`,
`created_at`,
`update_at`)
VALUES
(1,"coding dojo",now(),now()),
(2,"aml-sip",now(),now()),
(3,"sip-sanbernardo",now(),now());


-- Consulta: crea 3 ninjas que pertenezcan al primer dojo

INSERT INTO `asignaciones`.`ninjas`
(`id`,
`first_name`,
`last_name`,
`age`,
`dojo_id`,
`created_at`,
`update_at`)
VALUES
(1,"benjamin","herrera",17,1,now(),now()),
(2,"cristofer","gutierrez",20,1,now(),now()),
(3,"benjamin","castro",17,1,now(),now());

-- Consulta: crea 3 ninjas que pertenezcan al segundo dojo

INSERT INTO `asignaciones`.`ninjas`
(`id`,
`first_name`,
`last_name`,
`age`,
`dojo_id`,
`created_at`,
`update_at`)
VALUES
(4,"matias","pereira",17,2,now(),now()),
(5,"maximiliano","cardenas",20,2,now(),now()),
(6,"benjamin","gomez",17,2,now(),now());

-- Consulta: crea 3 ninjas que pertenezcan al tercer dojo

INSERT INTO `asignaciones`.`ninjas`
(`id`,
`first_name`,
`last_name`,
`age`,
`dojo_id`,
`created_at`,
`update_at`)
VALUES
(7,"pedro","perez",17,3,now(),now()),
(8,"juan","muños",20,3,now(),now()),
(9,"diego","gomez",17,3,now(),now());

-- Consulta: recupera todos los ninjas del primer dojo

select *
from ninjas
where dojo_id = 3;


-- Consulta: recupera el dojo del último ninja

select  dojo_id
from ninjas
where id = 9;