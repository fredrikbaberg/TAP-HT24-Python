# Multiplikationstabellen
# Vi behöver en funktion som kan ge oss multiplikationstabellen.
# Parametern "n" talar om vilket tals tabell vi ska skapa.
# Parametern "limit" talar om var vi ska sluta.
# Om vi till exempel frågar efter 3:ans tabell, med limit==4, ska programmet räkna ut:
# 3*1 = 3
# 3*2 = 6
# 3*3 = 9
# 3*4 = 12

# multiplication_table(3, 4) → [3, 6, 9, 12]

def multiplication_table(n, limit):
    return [n*val for val in range(1, limit+1)]

# Formulera krav och acceptanskriterier.
# Kör sedan red-green-refactor för varje acceptanskriterium.

# Krav: Returnera en lista med multiplikationstabellen för ett givet värde (n) och antal tal som ska beräknas (limit).
# AK: Givet limit 0, returnera en tom lista.
# AK: Givet ett tal n och limit 3, returnera [n, 2*n, 3*n].
