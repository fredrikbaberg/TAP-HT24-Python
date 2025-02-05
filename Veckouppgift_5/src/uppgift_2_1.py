# 2 Öva på TDD
# Samla ihop dina funktioner så att de ligger i en eller flera moduler. Importera och anropa dem från main.py, så att main-filen bara innehåller funktionsanrop.

# 1a Hitta på lämplig testdata till följande funktion, som omvandlar grader Celsius till grader Fahrenheit.
def c_to_f(degree):
    if degree < -273.15:
        return None
    return degree * 9 / 5 + 32
# Svar: -273.16 (None), 0 (32), 37.8 (100.04)

# 1b Vilka ekvivalensklasser har parametern degree?
# Svar: Flyttal större än eller lika med 273.15.

# 1c Skriv ett testfall.
# Svar: Se ../test/test_uppgift_2_1.py
