#obtener todos los clientes dentro de ciudad_id = 312

select city.city_id, customer.first_name,customer.last_name, customer.email,address.address,city.city, country.country from customer
inner join address on customer.address_id = address.address_id
inner join city on city.city_id = address.city_id
inner join country on country.country_id = city.country_id
where city.city_id = 312;

#obtener todas las películas de comedias

select film.film_id, film.title, film.description, film.release_year, film.rating,film.special_features, category.name from film_category
inner join category on film_category.category_id = category.category_id
inner join film on film.film_id = film_category.film_id
where category.name = "Comedy";

#obtener todas las películas por actor_id=5

select actor.actor_id, concat(actor.first_name," ", actor.last_name) as actor_name, film.title, film.description, film.release_year from film_actor
inner join film on film.film_id = film_actor.film_id
inner join actor on actor.actor_id = film_actor.actor_id
where actor.actor_id = 5;

#obtener todos los clientes en store_id=1 y dentro de estas ciudades (1, 42, 312 y 459)

select customer.first_name, customer.last_name, customer.email, address.address from customer
inner join store on store.store_id = customer.store_id
inner join address on address.address_id = customer.address_id
inner join city on city.city_id = address.city_id
where (city.city_id = 1 or city.city_id = 42 or city.city_id = 312 or city.city_id = 459) and store.store_id = 1;

#obtener todas las películas con una "calificación = G" y una "característica especial = detrás de escena", unidas por actor_id = 15

select film.title, film.description, film.release_year, film.rating, film.special_features from film
inner join film_actor on film_actor.film_id = film.film_id
inner join actor on actor.actor_id = film_actor.actor_id 
where film.rating = "G" and film.special_features like "%behind the scenes%" and actor.actor_id = 15;

#obtener todos los actores que se unieron al film_id = 369

select film.film_id, film.title, actor.actor_id, concat(actor.first_name," ",actor.last_name) as actor_name from film
inner join film_actor on film_actor.film_id = film.film_id
inner join actor on actor.actor_id = film_actor.actor_id
where film.film_id = 369;

#obtener todas las películas de drama con una tarifa de arriendo de 2,99

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre from film
inner join film_category on film_category.film_id = film.film_id
inner join category on category.category_id = film_category.category_id
where film.rental_rate = 2.99 and  category.name = "Drama";

#obtener todas las películas de acción que estén unidas por SANDRA KILMER

select film.title, film.description, film.release_year, film.rating, film.special_features, category.name as genre ,concat(actor.first_name," ",actor.last_name) as actor_name from film
inner join film_actor on film_actor.film_id = film.film_id
inner join actor on actor.actor_id = film_actor.actor_id
inner join film_category on film_category.film_id = film.film_id
inner join category on category.category_id = film_category.category_id
where category.name like "Action" and actor.first_name like "SANDRA" and actor.last_name like "KILMER";
