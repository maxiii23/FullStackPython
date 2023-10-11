from mascota import Mascota


class Ninja:
    def __init__(self,nombre, apellido, premios, comida_mascota, name, tipo, golosinas, salud, energia, sonido):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = Mascota(name, tipo, golosinas, salud, energia, sonido)

    def caminar(self):
        self.mascota.jugar()
        print(f"tu y tu mascota salieron a caminar")

    def alimentar(self):
        self.mascota.comer()
        print(f"alimentaste a tu mascota")       

    def bañar(self):
        self.mascota.sonido 
        print(f"bañaste a tu perro a tu perro")  
              


benjamin = Ninja("benjamin", "herrera", 12, 50, "cristofer", "perro", "croquetas", 50, 50, "Guau Guau" )


benjamin.alimentar()
benjamin.caminar()
benjamin.bañar()

# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
