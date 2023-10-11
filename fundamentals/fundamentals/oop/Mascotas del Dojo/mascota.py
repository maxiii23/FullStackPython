class Mascota:
    def __init__(self, name, tipo, golosinas, salud, energia, sonido):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.energia = energia
        self.salud = salud         
        self.sonido = sonido

    def dormir(self):
        self.energia +=25
        print(f"{self.name}ha dormido y su energia ha aumentado hasta {self.energia}")
        return self
    
    def comer(self):
        self.energia += 5
        self.salud += 10
        print(f"{self.name} ha comido su salud incremento a {self.salud} y su energia aumento a {self.energia}")
        return self

    def jugar(self):
        self.salud += 5
        print(f"{self.name} ha jugado su salud aumento a {self.salud}")
        return self
    
    def ruido(self):
        print(f"{self.sonido}")
        return self
'''
cristofer = Mascota("cristofer", "perro", "croquetas", 50, 50, "Guau Guau" )

cristofer.dormir()
cristofer.comer()
cristofer.jugar()
cristofer.ruido()

'''

# implementa __init__( name , tipo , golosinas ):
# implementa los siguientes métodos:
# dormir() - incrementa la energía de la mascota en 25
# comer() - incrementa la energía de la mascota en 5 y la salud en 10
# jugar() - incrementa la salud de la mascota en 5
# ruido() - imprime el sonido que produce la mascota
