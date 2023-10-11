class Usuario:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.balance = saldo_inicial

    def hacer_retiro(self, amount):
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
        else:
            self.balance -= amount
            print("Retiro exitoso. Saldo restante:", self.balance)

    def mostrar_balance(self):
        print("tu saldo es :", self.balance)

    def hacer_deposito(self, amount):
        self.balance += amount
        print("Depósito exitoso hacia. Saldo actual:", self.balance)     

    def tranferencia(self, amount,user):
        
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
        else:
            self.balance -= amount
            user.balance += amount
            print("Tu transferencia hacia",user.nombre,"fue exitosa. Tu saldo es :", self.balance)


juan = Usuario("Juan", 10000)
benjamin = Usuario("benjamin", 10000)
luis = Usuario("luis", 10000)


benjamin.mostrar_balance()
juan.hacer_deposito(100)
juan.hacer_deposito(100)
juan.hacer_deposito(100)
juan.hacer_retiro(400)
juan.mostrar_balance()
benjamin.hacer_deposito(100)
benjamin.hacer_deposito(100)
benjamin.hacer_retiro(400)
benjamin.hacer_retiro(180)
benjamin.mostrar_balance()
luis.hacer_deposito(300)
luis.hacer_retiro(100)
luis.hacer_retiro(100)
luis.mostrar_balance()
juan.tranferencia(100, luis)
luis.mostrar_balance()
juan.mostrar_balance()