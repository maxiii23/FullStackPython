from productos import producto 

class tiendita:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def mostrar_productos(self):
        for i in self.productos:
            print(f"{i.nombre}, {i.precio}, {i.categoria}. ")
        return self
    
    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
#este es utilizando length
    def vender_producto(self, id):
        index = 1
        for producto in self.productos: 
            indice = self.productos.index(producto)
            if indice == id:
                self.productos.pop(indice)
                print(f"Producto vendido: {producto.nombre}, Precio: {producto.precio}")
                return self
        else:
            print("El producto con el ID especificado no existe en la lista de productos de la tienda.")
#este es cun un id especificio asignado
    def vender_articulo(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                self.productos.remove(producto)
                print(f"Producto vendido: {producto.nombre}, Precio: {producto.precio}")
                return self
        print("El producto con el ID especificado no existe en la lista de productos de la tienda.")

    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento,True)
        print("La inflación ha sido aplicada a los productos de la tiendita.") 

    def liquidacion(self,categoria, porcentaje_descuento):
        for producto in self.productos:
                if producto.categoria == categoria:
                    producto.actualizar_precio(porcentaje_descuento,False)   
        print(f"Se ha aplicado un descuento del {porcentaje_descuento}% a todos los productos de la categoria '{categoria}'." )  
            
