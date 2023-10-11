#contador de 1 a 150
for x in range(1, 151):
    print(x)

#contador de 0 a 1000 de 5 en 5
for a in range(0, 1000, 5):
    print(a)

#  números enteros del 1 al 100. Si es divisible por 5, imprime "Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo".
for s in range(0, 101):
    if s%10==0:

        print("coding dojo")
    elif s%5==0:
        print("coding")  
    else:
        print(s)

#agrega los enteros impares del 0 al 500,000, e imprime la suma final.
suma = 0
for z in range(1, 500000, 2):
    suma += z
print( "la suma es ", suma)


#imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
for i in range(2018, 0, -4):
    print(i)

#establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult.
lowNum = 1
highNum = 20
mult = 3

for x in range(lowNum,highNum,mult):
    print(x)