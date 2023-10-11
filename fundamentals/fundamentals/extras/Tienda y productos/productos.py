class producto:
    id_actual = 0
    
    def __init__(self, nombre, precio, categoria):
        self.id = producto.id_actual
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        producto.id_actual += 1

        
    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100    

    def Print_info(self):
        print(f"{self.nombre}, Categoria:{self.categoria}, Precio:{self.precio}")






