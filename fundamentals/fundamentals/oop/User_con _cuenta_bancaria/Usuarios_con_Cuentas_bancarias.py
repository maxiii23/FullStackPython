class BancoAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BancoAccount.accounts.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def informacion_cuenta(self):
        return f"{self.balance}"

    def calcular_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, name):
        self.name = name
        self.account = {
            "comprobar" : BancoAccount(.02,1000),
            "ahorros" : BancoAccount(.05,3000)

        }
        

    def user_balance(self):
        print(f"User: {self.name}, comprobar {self.account['comprobar'].informacion_cuenta()}")
        print(f"User: {self.name}, ahorros {self.account['ahorros'].informacion_cuenta()}")
        return self

    def transferir_dinero(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

benja = User("benja")


benja.account['comprobar'].deposito(100)
benja.user_balance()
