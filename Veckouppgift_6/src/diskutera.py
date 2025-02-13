# 1 Läsa och förstå kod - diskutera i grupp
# Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE, exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?

# 1 Vad gör följande kod?
# Svar: Skapar objektet SafeStorage, lägger in Anakonda och Boaorm, samt skriver ut "Anakonda Boaorm".
print("--- 1 - Diskussion - 1")
class SafeStorage:
    __data = None
    def get(self):
        return self.__data
    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)


# 2a Vad gör följande kod? Fixa eventuella fel.
# Svar: Skapar en klass för Animal, med två klasser som ärver från Animal (Dog, Cat).
#       När make_noise anropas skrivs djurets ljud ut.
#       Fel:
#           * För Dog saknas en indentering vid print()
#           * För Cat kommer både standardutskriften och "Mjau!" skrivas ut, på grund av super().make_noise(); Cat använer shelf i stället för self.
#           * sound_off(animal) är inte anpassat för lista som indata.
print("--- 1 - Diskussion - 2a")
class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!") # Saknade indentering.

class Cat(Animal):
    def make_noise(self): # self, inte shelf.
        # super().make_noise() # Anropar förälderns funktion.
        print("Mjau!")

class Rooster(Animal): # Rooster saknades.
    def make_noise(self):
        print("Kuckeliku!")


def sound_off(animal):
    animal.make_noise()

c = Cat()
d = Dog()
h = Rooster()
for animal in [c, d, h]: # Tog inte hänsyn till lista
    sound_off(animal)

# 2b Lägg till en klass för ett annat djur, till exempel en guldfisk.
print("--- 1 - Diskussion - 2b")
class Goldfish(Animal): # Lagt till guldfisk
    def make_noise(self):
        print("Blubb!")

# Lagt till guldfisk
g = Goldfish()
sound_off(g)