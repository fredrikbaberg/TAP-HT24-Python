# 2a Betrakta funktionen count_words(sentence), som tar en sträng och returnerar antalet ord. Ett ord är en serie tecken som separeras av mellanslag. Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
# Svar:
# * Returnerar 0 om sentence är tom.
# * Returnerar 0 om sentence inte är en sträng.
# * Returnerar antal ord, uppdelade av mellanslag.

# 2b Skriv testfall som testar alla AK.
# Svar: Se test_uppgift_2_2.py

# 2c Implementera funktionen, så att alla testfall blir gröna.
def count_words(sentence):
    if not isinstance(sentence, str):
        return 0
    if len(sentence) == 0:
        return 0
    return len(sentence.split(" "))
