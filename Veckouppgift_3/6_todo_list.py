# 6 Todo list (att göra-lista)
# Bygg ett program där användaren kan lägga till saker till en todo-lista.
# Tips: använd en loop, input och en variabel för listan.

# Tester:
# - Visa lista - listan är tom
# - Tryck 2 och retur, skriv in text och tryck retur. Tryck 1. Listan visar det du skrev in.

print('''** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
Annat. Avsluta''')
uppgifter = []
while True:
    alternativ = input("Välj ett alternativ: ")
    if alternativ == '1':
        if len(uppgifter) == 0:
            print("Din lista är tom", end='')
        for uppgift in uppgifter:
            print("+ {}".format(uppgift))
        print(".")
    elif alternativ == '2':
        nyPost = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        uppgifter.append(nyPost)
        print(f"Ok, lade till \"{nyPost}\" i listan.")
    elif alternativ == '3': # Version 2
        attTaBort = input("Vilken grej är du färdig med? ")
        try:
            uppgifter.remove(attTaBort)
            print(f"ok, tog bort \"{attTaBort}\" från listan.")
        except ValueError:
            print("Det fanns inte på listan.")
    else:
        print("Felaktig inmatning, avslutar.")
        quit()
