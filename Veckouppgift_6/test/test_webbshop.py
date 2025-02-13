
from Veckouppgift_6.src.webbshop import Order, Product, ShoppingCart


def test_webbshop__skapa_produkt():
    # Skapa en produkt med ID, namn och pris
    expected = "1. Processor (2999)"
    actual = Product(id=1, name="Processor", price=2999).__str__()
    assert actual == expected

def test_webbshop__create_order():
    order = Order(id=1)
    cart = None
    order.add_shopping_cart(cart)
    assert order.shopping_carts == [None]

def test_webbshop__create_shopping_cart():
    cart = ShoppingCart(id=1)
    # Skapa 10 produkter
    products = [
        Product(1, "Processor (Intel i7)",	2999),
        Product(2, "Grafikkort (NVIDIA RTX 3060)",	4999),
        Product(3, "Moderkort (ASUS ROG)",	1899),
        Product(4, "SSD (Samsung 1TB)",	1299),
        Product(5, "RAM (Corsair 16GB)",	999),
        Product(6, "Nätaggregat (650W)",	899),
        Product(7, "CPU-kylare (Noctua)",	749),
        Product(8, "Chassi (NZXT)",	1099),
        Product(9, "Ljudkort (Creative)",	599),
        Product(10, "Optisk enhet (DVD-RW)",	349),
    ]
    # Lägg till alla produkter i kundvagnen.
    for product in products:
        cart.add_product(product)

    # Kontrollera att kundvagnen innehåller alla 10 produkter.
    assert len(cart.products) == 10
