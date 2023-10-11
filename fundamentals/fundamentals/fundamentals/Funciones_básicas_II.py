#contador hacia atras 
def countdown(a):
    c = []
    for b in range(a, -1, -1):
        c.append(b)
    return c
print(countdown(10))

#Imprimir y devolver

def imp_dev(a,b):
    print(a)
    return b
imp_dev(7,5)

#Primero más longitud
def suma_longitud(lista):
    return lista[0] + len(lista)
print(suma_longitud([1,2,3,4,5,5,3,6,2]))

#Valores mayores que el segundo
def filtrar_lista(lista):
    if len(lista) < 2:
        return False
    else:
        segundo_valor = lista[1] 
        nueva_lista = [valor for valor in lista if valor > segundo_valor]
        return nueva_lista
print(filtrar_lista([3,4,1,5,2,35,6,2,34,54,2,9,76,4,1]))   

#Esta longitud, ese valor
def crear_lista(tamaño, valor):
    return [valor] * tamaño
print(crear_lista(33,8))