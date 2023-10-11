-- obtener todos los países que hablan esloveno

SELECT c.`name` AS CountryName, l.`language` AS Language, l.`percentage` AS LanguagePercentage
FROM `countries` c
JOIN `languages` l ON c.`id` = l.`country_id`
WHERE l.`language` = 'Slovenian'
ORDER BY l.`percentage` DESC;

-- mostrar el número total de ciudades de cada país

SELECT c.`name` AS CountryName, l.`language` AS Language, COUNT(ct.`id`) AS TotalCities
FROM `countries` c
JOIN `languages` l ON c.`id` = l.`country_id`
JOIN `cities` ct ON c.`id` = ct.`country_id`
GROUP BY c.`name`, l.`language`
ORDER BY TotalCities DESC;

--  obtener todos ciudades de México con una población mayor a 500,000

SELECT `name` AS CityName, `population`
FROM `cities`
WHERE `country_code` = 'MEX' AND `population` > 500000
ORDER BY `population` DESC;

--  obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%

SELECT c.`name` AS CountryName, l.`language` AS Language, l.`percentage` AS LanguagePercentage
FROM `countries` c
JOIN `languages` l ON c.`id` = l.`country_id`
WHERE l.`percentage` > 89
ORDER BY l.`percentage` DESC;

-- obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000

SELECT `name` AS CountryName, `surface_area` AS SurfaceArea, `population`
FROM `countries`
WHERE `surface_area` < 501 AND `population` > 100000;

--obtener países solo con monarquía constitucional, un capital superior a 200 y una esperanza de vida mayor a 75 años

SELECT `name` AS CountryName, `government_form` AS GovernmentForm, `capital`, `life_expectancy`
FROM `countries`
WHERE `government_form` = 'Constitutional Monarchy' AND `capital` > 200 AND `life_expectancy` > 75;


-- obtener todas las ciudades de Argentina dentro del distrito de Buenos Aires con una población mayor a 500,000 habitantes

SELECT c.name AS CountryName, ct.name AS CityName, ct.district, ct.population
FROM countries c
JOIN cities ct ON c.code = ct.country_code
WHERE c.code = 'ARG' AND ct.district = 'Buenos Aires' AND ct.population > 500000;

--resumir el número de países en cada región

SELECT region AS RegionName, COUNT(*) AS NumberOfCountries
FROM countries
GROUP BY region
ORDER BY NumberOfCountries DESC;
