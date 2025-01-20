# 2 Öva på loopar och listor

# 1a Skriv färdigt kodexemplet.
answer = 0
for i in range(11):
    answer += i
print("Summan av talen 1 till 10 är: " + str(answer))
# Svaret ska bli 55

# 1b Räkna ut summan av alla tal mellan 1 och 100. (inklusive 1 och 100, rätt svar ska bli 5050)
summaFor = 0
for i in range(1,101):
    summaFor += i
print(f"Summan blir: {summaFor}")

# 1c Skriv om 1b så den använder en while-loop
summaWhile = 0
i = 0
while i <= 100:
    summaWhile += i
    i += 1
print(f"Summa med while blir: {summaWhile}")

# 2 Räkna ut summan av alla elementen i listan: [1, -2, 3, -2, 4, -3] 
lista = [1, -2, 3, -2, 4, -3]
summaLista = 0
for x in lista:
    summaLista += x
print(f"Summan av listan blir: {summaLista}")

# 3  Träna på att skapa och manipulera listor. Alla uppgifter ska lösas med funktionerna som står i presentationen.
# 3a Skapa en lista med namnen på fyra filmer. Namnen ska vara strängar. Skriv ut hela listan 2med funktionen print.
filmer = ['Star Wars Episod 4', 'Star Wars Episod 5', 'Star Wars Episod 6', 'Star Wars Episod 1']
print("Filmerna är: " + ', '.join(filmer))

# 3b Lägg till "Fellowship of the ring" sist i listan.
filmer.append('Fellowship of the ring')

# 3c Lägg till "The two towers" på första platsen i listan. (index noll)
filmer.insert(0, "The two towers")

# 3d Ta reda på vilken position (index) "Fellowship of the ring" har nu.
indexFellowshipOfTheRing = filmer.index("Fellowship of the ring")
print(indexFellowshipOfTheRing)

# 3e Ta bort en annan av filmerna. Har Fellowship-filmen ändrat index?
filmer.remove('Star Wars Episod 1')
print(filmer.index("Fellowship of the ring"))
# Ja, index har minskat med 1.

# 3f Ta reda på hur lång listan är. (len)
print(f"Listan har längden {len(filmer)}")

# 3g Vänd listan baklänges.
filmer.reverse()
print(','.join(filmer))

# 3h Sortera listan stigande i bokstavsordning.
filmer.sort()
print(','.join(filmer))
