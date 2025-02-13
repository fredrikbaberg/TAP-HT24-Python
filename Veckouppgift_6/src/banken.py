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
    # Konstruktor. Kan ange ett startsaldo, standard är 0.
    def __init__(self, initial_balance = 0.0):
        self.__balance = initial_balance

    # Gör en insättning på kontot, om insättningen är ett positivt värde.
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            # Felmeddelande vid negativ insättning.
            raise ValueError('Negativ insättning ej tillåten.')

    # Gör ett uttag, kollar först att det finns täckning på kontot.
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            return None
        
    # Kontrollera om det finns täckning på kontot för att betala en räkning.
    def can_pay_bill(self, amount):
        if self.__balance > amount:
            return True
        return False

    # Räkna ut ränta, anges i procent.
    def apply_interest(self, interest):
        self.__balance *= (100+interest)/100

    @property
    def balance(self): # Getter som returnerar saldo.
        return self.__balance
