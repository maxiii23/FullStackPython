class Usuario:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.balance = saldo_inicial

    def hacer_retiro(self, amount):
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
            return self
        else:
            self.balance -= amount
            print("Retiro exitoso. Saldo restante:", self.balance)
            return self

    def mostrar_balance(self):
        print(self.nombre ,"tu saldo es :", self.balance)
        return self

    def hacer_deposito(self, amount):
        self.balance += amount
        print("Deposito exitoso Saldo actual:", self.balance)   
        return self  

    def tranferencia(self, amount,user):
        
        if amount > self.balance :
            print("Error: no hay suficiente saldo en la cuenta")
            return self
        else:
            self.balance -= amount
            user.balance += amount
            print("Tu transferencia hacia",user.nombre,"fue exitosa. Tu saldo es :", self.balance)
            return self


juan = Usuario("Juan", 10000)
benjamin = Usuario("benjamin", 10000)
luis = Usuario("luis", 10000)

juan.hacer_deposito(100).hacer_deposito(100).hacer_deposito(100).hacer_retiro(400).mostrar_balance()
benjamin.hacer_deposito(100).hacer_deposito(100).hacer_retiro(400).hacer_retiro(180).mostrar_balance()
luis.hacer_deposito(300).hacer_retiro(100).hacer_retiro(100).mostrar_balance()
juan.tranferencia(100, luis).mostrar_balance()
luis.mostrar_balance()
