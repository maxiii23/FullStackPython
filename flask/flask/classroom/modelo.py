"""
[ brands]
[categories]
[customers]
[order_items]
[order]
[products]
[products]
[staffs]
[stocks]
[stores]
"""


class Category:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

class Brand:
    def __init__(self, brand_id, brand_name):
        self.brand_id = brand_id
        self.brand_name = brand_name

class Product:
    def __init__(self, product_id, product_name, brand_id, category_id, model_year, list_price):
        self.product_id = product_id
        self.product_name = product_name
        self.brand_id = brand_id
        self.category_id = category_id
        self.model_year = model_year
        self.list_price = list_price

class Customer:
    def __init__(self, customer_id, first_name, last_name, phone, email, street, city, state, zip_code):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Store:
    def __init__(self, store_id, store_name, phone, email, street, city, state, zip_code):
        self.store_id = store_id
        self.store_name = store_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

class Staff:
    def __init__(self, staff_id, first_name, last_name, email, phone, active, store_id, manager_id):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.active = active
        self.store_id = store_id
        self.manager_id = manager_id

class Order:
    def __init__(self, order_id, customer_id, order_status, order_date, required_date, shipped_date, store_id, staff_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.order_status = order_status
        self.order_date = order_date
        self.required_date = required_date
        self.shipped_date = shipped_date
        self.store_id = store_id
        self.staff_id = staff_id

class OrderItem:
    def __init__(self, order_id, item_id, product_id, quantity, list_price, discount):
        self.order_id = order_id
        self.item_id = item_id
        self.product_id = product_id
        self.quantity = quantity
        self.list_price = list_price
        self.discount = discount

class Stock:
    def __init__(self, store_id, product_id, quantity):
        self.store_id = store_id
        self.product_id = product_id
        self.quantity = quantity

class Products_Sales:
    def __init__(self, store_id, sucursal_venta, codigo_de_producto, nombre_del_producto, año_del_producto, precio_de_lista, cantidad_vendida_anual):
        self.store_id = store_id
        self.sucursal_venta = sucursal_venta
        self.codigo_de_producto = codigo_de_producto
        self.nombre_del_producto = nombre_del_producto
        self.año_del_producto = año_del_producto
        self.precio_de_lista = precio_de_lista
        self.cantidad_vendida_anual = cantidad_vendida_anual
