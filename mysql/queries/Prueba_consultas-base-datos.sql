-- ------------------------------------------------------  caso 1   --------------------------------------------------------------------------------------------------
SELECT
p.product_id AS PRODUCTO,
    p.product_name AS 'NOMBRE DE PRODUCTOS',
    b.brand_name AS MARCA,
    c.category_name AS CATEGORIA,
    p.model_year AS 'AÑO MODELO',
    YEAR(CURDATE()) - p.model_year AS ANTIGUEDAD,
    p.list_price AS 'PRECIO DE LISTA',
    CASE
        WHEN p.model_year = YEAR(CURDATE()) - 1 THEN ROUND(p.list_price * 0.9, 2)
        WHEN p.model_year = YEAR(CURDATE()) - 2 THEN ROUND(p.list_price * 0.8, 2)
        ELSE ROUND(p.list_price * 0.75, 2)
    END AS 'PRECIO DE LISTA CON DESCUENTO'
FROM
    products p
JOIN
    brands b ON p.brand_id = b.brand_id
JOIN
    categories c ON p.category_id = c.category_id
ORDER BY
    b.brand_name,
    c.category_name,
    p.model_year,
    p.list_price;
    
    






------------------------------------------------------  caso 2   --------------------------------------------------------------------------------------------------

SELECT
    ventas_por_sucursal.Periodo,
    ventas_por_sucursal.Sucursal,
    ventas_por_sucursal.Direccion_Sucursal,
    ventas_por_sucursal.Cantidad_Total_de_Ventas,
    ventas_por_sucursal.Total_Venta,
    ventas_por_sucursal.Venta_Promedio,
    ventas_por_sucursal.Total_de_Productos_Vendidos
FROM
    (SELECT
        2017 AS PERIODO,
        s.store_id,
        s.store_name AS Sucursal,
        CONCAT(s.street, ', ', s.city, ', ', s.state, ', ', s.zip_code) AS Direccion_Sucursal,
        COUNT(o.order_id) AS Cantidad_Total_de_Ventas,
        SUM(oi.list_price) AS Total_Venta,
        AVG(oi.list_price) AS Venta_Promedio,
        SUM(oi.quantity) AS Total_de_Productos_Vendidos
  FROM
        stores s
    JOIN
        orders o ON s.store_id = o.store_id
    JOIN
        order_items oi ON o.order_id = oi.order_id
    WHERE
        YEAR(o.order_date) = 2017
    GROUP BY
        s.store_id, s.store_name
    ORDER BY
        Total_Venta asc
    LIMIT 1) AS ventas_por_sucursal

UNION ALL

SELECT
    ventas_por_sucursal.Periodo,
    ventas_por_sucursal.Sucursal,
    ventas_por_sucursal.Direccion_Sucursal,
    ventas_por_sucursal.Cantidad_Total_de_Ventas,
    ventas_por_sucursal.Total_Venta,
    ventas_por_sucursal.Venta_Promedio,
    ventas_por_sucursal.Total_de_Productos_Vendidos
FROM
    (SELECT
        2017 AS PERIODO,
        s.store_id,
        s.store_name AS SUCURSAL,
        CONCAT(s.street, ', ', s.city, ', ', s.state, ', ', s.zip_code) AS Direccion_Sucursal,
        COUNT(o.order_id) AS Cantidad_Total_de_Ventas,
		AVG(oi.list_price) AS Venta_Promedio,
		SUM(oi.list_price) AS Total_Venta,
        SUM(oi.quantity) AS Total_de_Productos_Vendidos
  
    
     FROM
        stores s
    JOIN
        orders o ON s.store_id = o.store_id
    JOIN
        order_items oi ON o.order_id = oi.order_id
	WHERE
        YEAR(o.order_date) = 2017
    
    GROUP BY
        s.store_id, s.store_name
    ORDER BY
        Total_Venta desc
    LIMIT 1) AS ventas_por_sucursal



-----------------------------------------  caso 3.1  ------------------------------------------------------------------------------

SELECT
	ventas_2017.Codigo_de_producto,
	ventas_2017.Nombre_del_producto,
	ventas_2017.Anio_del_producto,
	ventas_2017.store_id,
    ventas_2017.Precio_de_lista,
    ventas_2018.Cantidad_vendida_2018
FROM
    (SELECT
        s.store_id,
        s.store_name AS Sucursal_de_venta,
        p.product_id AS Codigo_de_producto,
        p.product_name AS Nombre_del_producto,
        p.model_year AS Anio_del_producto,
        p.list_price AS Precio_de_lista,
        SUM(oi.quantity) AS Cantidad_vendida_2017
    FROM
        products p
    JOIN
        order_items oi ON p.product_id = oi.product_id
    JOIN
        orders o ON oi.order_id = o.order_id
    JOIN
        stores s ON o.store_id = s.store_id
    WHERE
        YEAR(o.order_date) = 2017
    GROUP BY
        s.store_id, s.store_name, p.product_id, p.product_name, p.model_year, p.list_price) AS ventas_2017

JOIN

    (SELECT
        s.store_id,
        s.store_name AS Sucursal_de_venta,
        p.product_id AS Codigo_de_producto,
        SUM(oi.quantity) AS Cantidad_vendida_2018
    FROM
        products p
    JOIN
        order_items oi ON p.product_id = oi.product_id
    JOIN
        orders o ON oi.order_id = o.order_id
    JOIN
        stores s ON o.store_id = s.store_id
    WHERE
        YEAR(o.order_date) = 2018
    GROUP BY
        s.store_id, s.store_name, p.product_id) AS ventas_2018

ON ventas_2017.store_id = ventas_2018.store_id AND ventas_2017.Codigo_de_producto = ventas_2018.Codigo_de_producto
WHERE ventas_2017.Cantidad_vendida_2017 = ventas_2018.Cantidad_vendida_2018
ORDER BY
    	store_id , ventas_2017.Nombre_del_producto;


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-- Crear la nueva tabla products_sales
CREATE TABLE products_sales (
    store_id INT,
    Sucursal_de_venta VARCHAR(255),
    Codigo_de_producto INT,
    Nombre_del_producto VARCHAR(255),
    Anio_del_producto INT,
    Precio_de_lista DECIMAL(10, 2),
    Cantidad_vendida_2017 INT,
    Cantidad_vendida_2018 INT
);

-- Insertar los datos en la tabla products_sales desde la consulta
INSERT INTO products_sales (store_id, Sucursal_de_venta, Codigo_de_producto, Nombre_del_producto, Anio_del_producto, Precio_de_lista, Cantidad_vendida_2017, Cantidad_vendida_2018)
SELECT
    ventas_2017.store_id,
    ventas_2017.Sucursal_de_venta,
    ventas_2017.Codigo_de_producto,
    ventas_2017.Nombre_del_producto,
    ventas_2017.Anio_del_producto,
    ventas_2017.Precio_de_lista,
    ventas_2017.Cantidad_vendida_2017,
    ventas_2018.Cantidad_vendida_2018

    --------------------------------------------------------------------------
 
    -- Actualizar nombre del producto y precio de lista en la tabla products
UPDATE products
SET
    product_name = CONCAT(product_name, ' (Oferta Especial)'),
    list_price = list_price / 2
WHERE
    product_id = true
    ;