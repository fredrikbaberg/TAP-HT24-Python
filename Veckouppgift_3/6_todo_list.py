# 6 Todo list (att göra-lista)
# Bygg ett program där användaren kan lägga till saker till en todo-lista.
# Tips: använd en loop, input och en variabel för listan.
#
# Version 2: lägg till ett menyalternativ, "Markera som klar". När användaren väljer det, ska programmet fråga efter vilken grej man är färdig med. Den färdiga grejen ska tas bort från listan.
# Version 3: lägg över färdiga grejer i en ny lista. Användaren ska kunna välja vad man har bockat av tidigare, eller välja att lägga tillbaka grejen i todo-listan.

# Tester:
# - Version 1
#   1. Visa lista - listan är tom
#   2. Skriv 2, tryck retur, skriv in text1, tryck retur, skriv 1, tryck retur. Listan visar vad du skrev in.
#   3. Skriv 2, tryck retur, skriv in text2, tryck retur, skriv 1, tryck retur. Listan innehåller två punkter.
# - Version 2
#   1. Genomför steg för version 1
#   2. Skriv 3, tryck retur, skriv in text1, tryck retur, skriv 1, tryck retur. Listan innehåller endast text2.
#   3. Skriv 3, tryck retur, skriv in text9, tryck retur, få meddelande att det inte gick. Skriv 1, tryck retur, listan innehåller endast text2.
# - Version 3
#   1. Genomför steg för version 2
#   2. Skriv 4, tryck retur, välj 0, tryck retur, skriv 1, tryck retur. Listan innehåller text1 och text2.


print('''** Todo list extravaganza **
1. Se innehållet i din lista
2. Lägga till nya punkter i din lista
3. Markera som klar
4. Markera klar som ej klar
Allt annat. Avsluta''')

uppgifter = []
fardigaUppgifter = []

while True:
    alternativ = input("Välj ett alternativ: ")
    if alternativ == '1':
        if len(uppgifter) == 0:
            print("Din lista är tom")
        for uppgift in uppgifter:
            print("+ {}".format(uppgift))
        print(".")

    elif alternativ == '2':
        nyPost = input("Skriv in en ny sak du måste komma ihåg att göra: ")
        uppgifter.append(nyPost)
        print(f"Ok, lade till \"{nyPost}\" i listan.")

    elif alternativ == '3':
        klar = input("Vilken grej är du färdig med? ")
        try:
            uppgifter.remove(klar)
            fardigaUppgifter.append(klar)
            print(f"ok, tog bort \"{klar}\" från listan.")
        except ValueError:
            print("Det fanns inte på listan.")

    elif alternativ == '4':
        print("Färdiga grejer:")
        for i in range(len(fardigaUppgifter)):
            print(f"{i}. {fardigaUppgifter[i]}")
        try:
            laggTillbaka = int(input("Vad vill du lägga tillbaka? Ange numret som raden börjar med. "))
            if laggTillbaka in range(len(fardigaUppgifter)):
                tmp = fardigaUppgifter[laggTillbaka]
                uppgifter.append(tmp)
                try:
                    fardigaUppgifter.remove(tmp)
                    print(f"Lagt tillbaka {tmp} i listan.")
                except ValueError:
                    print(f"Misslyckades att flytta {tmp} till att göra-listan.")
        except ValueError:
            print("Felaktig inmatning.")

    else:
        print("Avslutar.")
        quit()
