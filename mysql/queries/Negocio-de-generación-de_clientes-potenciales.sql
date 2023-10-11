##1. ¿Qué consulta ejecutarías para obtener los ingresos totales de marzo de 2012?

SELECT SUM(b.amount) AS ingresos_totales_de_marzo
FROM billing AS b
JOIN clients AS c ON b.client_id = c.client_id
WHERE DATE_FORMAT(b.charged_datetime, '%Y-%m') = '2012-03';


##2. ¿Qué consulta ejecutarías para obtener los ingresos totales recaudados del cliente con id de 2?

SELECT SUM(amount) AS ingresos_totales
FROM billing
WHERE client_id = 2;


##3. ¿Qué consulta ejecutarías para obtener todos los sitios que posee el cliente con id de 10?

SELECT domain_name, client_id 
FROM sites
WHERE client_id = 10;

##4. ¿Qué consulta ejecutarías para obtener el número total de sitios creados por mes por año para el cliente con id de 1? ¿Qué pasa con el cliente con id de 20?

SELECT
    YEAR(created_datetime) AS year,
    MONTH(created_datetime) AS month,
    COUNT(*) AS total_sites_created
FROM sites
WHERE client_id = 1
GROUP BY YEAR(created_datetime), MONTH(created_datetime)
ORDER BY year, month;


##5. ¿Qué consulta ejecutarías para obtener el número total de clientes potenciales generados para cada uno de los sitios entre el 1 de enero de 2011 y el 15 de febrero de 2011?

SELECT
    s.domain_name,
    COUNT(l.leads_id) AS total_leads_generated
FROM sites AS s
LEFT JOIN leads AS l ON s.site_id = l.site_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-02-15'
GROUP BY s.site_id;

##6. ¿Qué consulta ejecutarías para obtener el número total de clientes potenciales que hemos generado para cada uno de nuestros clientes entre el 1 de enero de 2011 y el 31 de diciembre de 2011?

SELECT
    c.client_id,
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    COUNT(l.leads_id) AS total_leads_generated
FROM clients AS c
LEFT JOIN sites AS s ON c.client_id = s.client_id
LEFT JOIN leads AS l ON s.site_id = l.site_id
WHERE l.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY c.client_id, client_name
ORDER BY total_leads_generated DESC;

##7. ¿Qué consulta ejecutarías para obtener una lista de nombres de clientes y el número total de clientes potenciales que hemos generado para cada cliente, cada mes, entre los meses 1 y 6 del año 2011?

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    MONTHNAME(l.registered_datetime) AS month,
    COUNT(l.leads_id) AS total_leads_generated
FROM clients AS c
LEFT JOIN sites AS s ON c.client_id = s.client_id
LEFT JOIN leads AS l ON s.site_id = l.site_id
WHERE YEAR(l.registered_datetime) = 2011
    AND MONTH(l.registered_datetime) BETWEEN 1 AND 6
GROUP BY client_name, month
ORDER BY month, month DESC;

##8. ¿Qué consulta ejecutarías para obtener una lista de nombres de clientes y el número total de clientes potenciales que hemos generado para cada uno de los sitios de nuestros clientes entre el 1 de enero de 2011 y el 31 de diciembre de 2011? 

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    s.domain_name,
    COUNT(l.leads_id) AS number_of_leads
FROM clients AS c
LEFT JOIN sites AS s ON c.client_id = s.client_id
LEFT JOIN leads AS l ON s.site_id = l.site_id
GROUP BY c.client_id, client_name, s.site_id
ORDER BY number_of_leads, s.site_id;


##9. Escribe una única consulta que recupere los ingresos totales recaudados por cada cliente durante cada mes del año. 
#9a
SELECT
    c.client_id,
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    YEAR(b.charged_datetime) AS year,
    MONTH(b.charged_datetime) AS month,
    SUM(b.amount) AS total_income
FROM clients AS c
LEFT JOIN billing AS b ON c.client_id = b.client_id
GROUP BY c.client_id, client_name, year, month
ORDER BY c.client_id, year, month;

#9b
SELECT
    c.client_id,
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    YEAR(b.charged_datetime) AS year,
    MONTH(b.charged_datetime) AS month,
    SUM(b.amount) AS total_income
FROM clients AS c
LEFT JOIN billing AS b ON c.client_id = b.client_id
GROUP BY c.client_id, client_name, year, month
ORDER BY c.client_id, year, month;
  (
    SELECT MONTHNAME(charged_datetime) 
    FROM billing AS sub_b 
    WHERE sub_b.client_id = c.client_id 
      AND MONTH(sub_b.charged_datetime) = month 
      AND YEAR(sub_b.charged_datetime) = year 
    LIMIT 1
  )


##10. Escribe una única consulta que recupere todos los sitios que posee cada cliente. 

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS client_name,
    GROUP_CONCAT(s.domain_name ORDER BY s.site_id SEPARATOR ', ') AS sitios
FROM clients AS c
LEFT JOIN sites AS s ON c.client_id = s.client_id
GROUP BY c.client_id, client_name
ORDER BY c.client_id;
