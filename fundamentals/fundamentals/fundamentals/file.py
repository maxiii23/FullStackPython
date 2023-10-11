num1 = 42 #declaración de variables
num2 = 2.3 #declaración de variables
boolean = True #declaración de variables
string = 'Hello World' #declaración de variables
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #List 
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}    # tuplas
fruit = ('blueberry', 'strawberry', 'banana') #List 
print(type(fruit)) #    - return
print(pizza_toppings[1]) #    - return
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #    - return
person['name'] = 'George'  #Data Types
person['eye_color'] = 'blue' #Data Types
print(fruit[2]) #    - return

if num1 > 45: #if 
    print("It's greater")  #    - return
else: #else
    print("It's lower") #    - return

if len(string) < 5: #if
    print("It's a short word!") #if
elif len(string) > 15: #else if
    print("It's a long word!") #    - return
else: #else
    print("Just right!") #    - return 

for x in range(5): #for loop
    print(x) #    - return
for x in range(2,5): #for loop
    print(x)#    - return
for x in range(2,10,3): #for loop
    print(x) #    - return
x = 0
while(x < 5):  #while loop
    print(x) #    - return
    x += 1

pizza_toppings.pop() #- delete value
pizza_toppings.pop(1) #- delete value

print(person) #    - return
person.pop('eye_color') #- delete value
print(person) #    - return

for topping in pizza_toppings:  #for loop
    if topping == 'Pepperoni': #if
        continue 
    print('After 1st if statement')
    if topping == 'Olives': #if
        break

def print_hello_ten_times(): #add value
    for num in range(10): #for loop
        print('Hello') #    - return

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello') #    - return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello') #    - return

print_hello_x_or_ten_times() #    - return
print_hello_x_or_ten_times(4) #    - return



"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)