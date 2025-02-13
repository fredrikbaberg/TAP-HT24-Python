# 2 Länder

# 1a På Island bor det 383726 invånare och i Danmark 5961249.
# Skapa objekt för länderna. (Data från januari 2024. Avrunda befolkningen.)
class Country:
    def __init__(self, name, pop, area=None):
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = []

    def __str__(self):
        # Delat upp strängen i flera delar, för läsbarhet.
        return "".join([
            f"I {self.__name} bor det {self.__population} miljoner invånare.",
            # Area läggs endast till om den är satt.
            (f" Arean är {self.__area} km^2" if self.__area is not None else ""),
            # Språk läggs endast till om det är satt.
            (f"\nOfficiella språk är: {", ".join(self.__languages)}." if len(self.__languages) > 0 else "")
        ])
    
    # Lägg till ett språk i taget.
    def add_language(self, language):
        self.__languages.append(language)
    
    @property
    def area(self):
        # Använder getter för area.
        return self.__area
    
    @property
    def languages(self):
        # Använder getter för språk
        return self.__languages

se = Country("Sverige", 10.5)
no = Country("Norge", 5.5)
dk = Country("Danmark", 6.0)
il = Country("Island", 0.4) # il i stället för is, eftersom det är ett reserverat ord.

# 1b Lägg till en metod med namnet "print_info". Om man anropar den för Sverige-objektet ska den skriva ut: "I Sverige bor det 10.5 miljoner invånare". Funktionen ska använda sina egenskaper, så att den fungerar för de andra länderna också.
for land in [se, no, dk, il]:
    print(land)

# 1c Lägg till landets area som en egenskap till klassen. Använd en parameter till konstruktorn, alltså __init__ metoden. Ge arean ett default värde på None så att man inte måste ange arean när man skapar ett landsobjekt.
# Exempel på default värde för en vanlig funktion:
# # y har default värde 10
# def exempel(x, y=10):
#     print(x + y)

# exempel(2)  # skriver ut 12

# 1d Ändra i metoden "print_info" så att den skriver ut arean också, men bara om arean inte är None.

# 1e Skapa en ny metod med namnet "add_language". Den ska lägga till ett av landets officiella språk. (Sverige har bara ett, men Finland har två språk (svenska och finska) och Schweiz har fyra.) För att kunna spara ett varierande antal behöver du använda en lista.

# 1f Ändra i "print_info" så att den skriver ut alla officiella språk, på en ny rad.
