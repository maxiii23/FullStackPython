'''
#1
def número_de_grupos_alimentarios():
    return 5
print(número_de_grupos_alimentarios())
# lo que retorna es 5 ya que en el retorno de la variable "número_de_grupos_alimentarios" es igual a 5 

#2
def número_de_ramas_militares():
    return 5
print(número_de_días_en_una_semana_silicona_o_lados_del_triángulo() + número_de_ramas_militares())
# daria error ya que "número_de_días_en_una_semana_silicona_o_lados_del_triángulo" no esta definido previamente en algun arreglo

#3
def número_de_libros_en_espera():
    return 5
    return 10
print(número_de_libros_en_espera())

# dara como resultado 5 ya que el 2°do return no lo tendra en cuenta al ser una repuesta 2° en una funcion

#4
def número_de_dedos():
    return 5
    print(10)
print(número_de_dedos())

# imprimira el valor de 5 ya que el print que hay esta dentro de de la funcion "número_de_dedos"
#5
def número_de_lagos_grandes():
    print(5)
x = número_de_lagos_grandes()
print(x)

#lo que imprime es "5" seguido de "none" ya que "print(x)" ya que la variable x no tiene una declaracion de retorno 

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# dara los resultados de 1+2 y 2+3 y luego dara un TyoeError ya  que no podemos sumar 2 funciones que no retornan ningun valor


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#esto dara "25" ya que los valores de 2 y 5 los comvierte en texto y al sumarse los sumara como cadena


#8
def número_de_océanos_o_dedos_o_continentes():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(número_de_océanos_o_dedos_o_continentes())


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# esto dara como resultado 7 ya que 2 es menor que 3 y se cumple el primer if 
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#esto dara 14 ya que 5 es mayor que 3 y se cumple el else
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#estodara 21 ya que al sumarse los 2 valores "7 y 14" dara este resultado

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#esto dara 8 ya que llama a la funcion y sumara los 2 valores que le demos (el segundo returnno ara nada)


#11
b = 500
print(b)
#esto dara 500 ya que imprime 500
def foobar():
    b = 300
    print(b)
print(b)
#esto imprime 500 ya que llamamos denuevo a "b" 
foobar()
#esto dara 300 ya que en la funcion llama a "b" dentro de esta misma y lo imprime 
print(b) 
#esto imprime 500 ya que llamamos denuevo a "b" 


#12
b = 500
print(b)
#esto dara 500 ya que llama a "b" 
def foobar():
    b = 300
    print(b)
    return b
print(b)
#dara 500 ya que llama de nuevo a 'b' 
foobar()
#esto llama a la funcion que imprime 300 ya que en la funciopn tenemos un print (el retur no ara nada ya estamis llamando a la funcion y no imprimiendola)
print(b)
#dara 500 ya que llama de nuevo a 'b'


#13
b = 500
print(b)
#esto dara 500 ya que "b" es igual a esto
def foobar():
    b = 300
    print(b)
    return b
print(b)
#dara 500 ya que llama de nuevo a 'b'
b=foobar()
#esto dara 300 ya que llama a la funcion
print(b)
#esto dara 300 ya que se le asigno un nuevo valor a "b" que sera 300 


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#esto dara "1", "3"y "2" ya que la funcion foo imprime primero 1 luego llama a bar (que es 3) y luego imprime 2
'''
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
#esto dara un valor a y 
print(y)
#imprimira y que sera 1, 3, 5, 10




