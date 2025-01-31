# Bygg en funktion som slumpar ett spelkort. Den ska returnera en lista med två element: färg och valör. Färg kan vara: ruter, hjärter, spader eller klöver. Valör kan vara tvåa till ess, för enkelhets skull använder vi talen 2 till 14.
from random import randint

def slumpa_spelkort():
    # Givet en lista med färger, slumpa ett index och returnera elementet i listan.
    farg = ["ruter", "hjärter", "spader", "klöver"][randint(0,3)]
    # Slumpa en valör mellan 2 och 14 (inklusive ändpunkter).
    valor = randint(2, 14)

    return [farg, valor]

# Testa funktionen genom att slumpa ett eller flera kort och skriv ut resultatet.
def test_slumpa_spelkort(antal):
    print(f"Slumpar {antal} kort: ", end='')
    # Skapa en lista med 'antal' kort. Använder _ som index eftersom det inte används.
    hand = [slumpa_spelkort() for _ in range(antal)]
    print(hand)
    print(f"Antal kort i listan {'stämmer' if len(hand)==antal else 'stämmer inte'}.")

# Gör det möjligt att anropa filen och då köra test.
if __name__=='__main__':
    test_slumpa_spelkort(5)
