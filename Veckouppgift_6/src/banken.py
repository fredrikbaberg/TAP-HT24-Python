# 3 Banken
# Skapa en klass som representerar ett bankkonto. Banken ska kunna:
# sätta in pengar (deposit)
# ta up pengar (withdraw)
# returnera nuvarande saldo (balance)
# räkna ut ränta (apply_interest, lägger till räntan till kontot)
# tala om ifall man har råd att betala en räkning (returnera True/False)

# Gör en metod för varje funktion.

# Skriv enhetstester för varje funktion. Använd gärna TDD-metoden, att börja med testfallen innan du skriver koden.

class Account():
    def __init__(self, initial_balance = 0.0):
        self.__balance = initial_balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            return None
        
    def can_pay_bill(self, amount):
        if self.__balance > amount:
            return True
        return False

    """ Räkna ut ränta, ange i procent."""
    def apply_interest(self, interest):
        self.__balance *= (100+interest)/100

    @property
    def balance(self):
        return self.__balance
