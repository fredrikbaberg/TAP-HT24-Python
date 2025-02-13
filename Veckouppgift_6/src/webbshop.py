# 4 Webbshop
# Skapa klasser som representerar en webbshop:
# produkter (Product)
# beställningar (Order)
# kundvagn (ShoppingCart)

# Tips 1! Ge varje klass en egenskap "__id". Man kan använda den för att referera till ett annat objekt. Detta behövs eftersom både kundvagn och beställningar kommer att innehålla befintliga produkter.

# Tips 2! Du kan använda AI för att skapa realistisk testdata. Prova till att börja med:
# "Skapa testdata för 10 produkter till en webbshop, som säljer verktyg. Visa datan i en tabell. Varje produkt ska ha namn, pris och ett unikt id."

# Klass för produkt. Har egenskaperna id, namn, pris.
class Product():
    def __init__(self, id, name, price):
        self.__id = id
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__id}. {self.__name} ({self.__price})"

# Klass för beställningar. Har egenskaperna id och en lista med kundvagnar.
class Order():
    def __init__(self, id):
        self.__shopping_carts = []
        self.__id = id

    # Kan lägga till en kundvagn i beställningar.
    def add_shopping_cart(self, cart):
        self.__shopping_carts.append(cart)

    @property
    def shopping_carts(self):
        return self.__shopping_carts

# Klass för kundvagn. Har egenskaperna id och produkter.
class ShoppingCart():
    def __init__(self, id):
        self.__id = id
        self.__products = []

    # Kan lägga till en produkt i kundvagnen.
    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return self.__products
