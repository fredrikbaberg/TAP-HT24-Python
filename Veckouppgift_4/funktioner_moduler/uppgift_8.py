# Gör en funktion som kan skriva ut innehållet i en lista lite snyggare. Först ska funktionen tala om ifall listan är tom, eller hur många element den har. Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
# pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14

def pretty_print(lista):
    print(f"Listan har {len(lista)} element:" if len(lista) > 0 else "Listan är tom")
    for i in range(len(lista)):
        print(f"{i}. {lista[i]}")
