# 1. Summera tre tal.
tal_1_in = input("Ange tal 1: ")
tal_2_in = input("Ange tal 2: ")
tal_3_in = input("Ange tal 3: ")

tal_1 = float(tal_1_in)
tal_2 = float(tal_2_in)
tal_3 = float(tal_3_in)
summa = tal_1 + tal_2 + tal_3
print("Summa: " + str(summa))

# 2. Hitta största talet (utan att använda max).
# Använder flera if/elif/else.
storsta_tal = 0 # Startvärdet skrivs över nedan.
if((tal_1 >= tal_2) and (tal_1 >= tal_3)): # >=, annars blir det problem när två tal är lika stora.
    storsta_tal = tal_1
elif((tal_2 >= tal_1) and (tal_2 >= tal_3)):
    storsta_tal = tal_2
else:
    storsta_tal = tal_3
print("Största talet är ", storsta_tal)

# 3. Tala om om två eller fler tal är lika.
alla_olika = True
if(tal_1 == tal_2 or tal_1 == tal_3 or tal_2 == tal_3):
    if(tal_1 == tal_2 == tal_3):
        print("Alla tre tal är lika")
    else:
        print("Två av talen är lika")
    alla_olika = False

# 4. Tala om vilket som är det mellersta talet. Alla tal måste vara olika.
if(alla_olika):
    # Hitta minsta talet. Använder en lista (egentligen nästa lektion).
    minsta_tal = tal_1
    for tal in [tal_2, tal_3]:
        if tal < minsta_tal:
            minsta_tal = tal
    # print("Minsta talet är ", minsta_tal)
    # Ta fram mellersta talet baserat på största och minsta.
    mellersta_tal = 0
    if (minsta_tal < tal_1 < storsta_tal):
        mellersta_tal = tal_1
    elif (minsta_tal < tal_2 < storsta_tal):
        mellersta_tal = tal_2
    else:
        mellersta_tal = tal_3
    print("Mellersta talet är", mellersta_tal)

# Testtabell
"""
t1 | t2 | t3 | Störst | Två lika? | Tre lika? | Mellerst?
 1    2    3    3        Nej         Nej         2
 1    3    2    3        Nej         Nej         2
 3    2    1    3        Nej         Nej         2
-1   -3   -1    3        Ja          Nej         -
 9    9    9    9        Ja          Ja          -
 32  32   16   32        Ja          Nej         -
"""