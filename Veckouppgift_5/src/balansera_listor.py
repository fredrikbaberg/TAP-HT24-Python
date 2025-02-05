# Balansera listor
# Som en del i ett större program har vi en lista som kan innehålla flera element. Men elementen kan flyttas mellan denna och en annan lista. Vi behöver ett sätt att balansera listorna, så att de har lika många element - åtminstone så nära som möjligt. Ordningen på elementen är inte viktig.
def balansera_listor(lista1, lista2):
    if (abs(len(lista1)-len(lista2))) < 2:
        return lista1, lista2
    while len(lista1) > len(lista2):
        lista2.append(lista1.pop())
    while len(lista2) > len(lista1):
        lista1.append(lista2.pop())
    return lista1, lista2

# Formulera krav och acceptanskriterier.
# Svar:
# Krav: Givet två listor, fördela elementen så listorna är lika långa.
# AK: Givet två listor med N element vardera, returnera listorna som de är.
# AK: Givet två listor med längdskillnad 1, returnera listorna som de är.
# AK: Givet en lista med 2*N element och en med 0 element, returnera två listor med N element var.
# AK: Givet en lista med 2*N+1 element och en med 0 element, returnera en lista med N+1 element och en med N element.

# Kör sedan red-green-refactor för varje acceptanskriterium.
