# 3 Kvittouträknaren
# Gör ett program som upprepade gånger ber användaren skriva in ett tal. När man skriver in strängen "quit" eller "avsluta" ska programmet ska det räkna ut summan av talen.
print("Välkommen till Kvittokompis! Avsluta genom att skriva: quit")
summa = 0
while True:
    belopp = input('Skriv in ett belopp: ')
    if belopp in ["quit", "avsluta"]:
        break
    try:
        summa += int(belopp)
    except ValueError:
        print("Misslyckades med att summera.")
print(f"Det blir {summa} kr totalt. Välkommen åter!")

# Version 2
antal = input("Hur många är ni? ")
print(f"Det blir {summa} kr totalt, alltså {summa/float(antal)} kr per person. Välkommen åter!")

# Version 3
# programmet ska fråga hur många procent dricks man vill lägga på. Om användaren inte skriver något (tom sträng) ska programmet använda 10% som standardinställning.
inputDricks = input("Hur mycket dricks vill du lägga till? (standard: 10%) ").replace("%","")
if inputDricks == '':
    dricks = 10
else:
    try:
        dricks = float(inputDricks)
        if dricks < 0:
            print("Du kan inte lämna negativ dricks.")
    except:
        dricks = 10

summaMedDricks = summa*(1+dricks/100)
print(f"Det blir {summaMedDricks} kr totalt med dricks, alltså {summaMedDricks/float(antal)} kr per person. Välkommen åter!")