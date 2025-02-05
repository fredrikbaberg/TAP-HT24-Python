# Söka efter användare
# Tänk dig en funktion som kan användas för att visa sökresultat medan användaren skriver i ett sökfält. Funktionen ska ta två parametrar: input är det användaren skriver, master_list är en lista med alternativ som kan hittas.
def autocomplete_list(input_string, master_list):
    if input_string == "":
        return []
    output_list = [s for s in master_list if input_string in s]
    # for s in master_list:
    #     if input_string
    # values = lambda x: x if x in master_list
    return output_list

# Börja med att formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
# Svar:
# * Krav: Givet en textsträng och en lista med alternativ, returnera en lista med alla entiteter i alternativ som matchar input.
# * AK: Givet en tom lista med alternativ, returnera en tom lista oavsett textsträng.
# * AK: Givet en tom textsträng, returnera en tom lista.
# * AK: Givet en textsträng och en lista med alternativ, returnera en lista med alla alternatv som matchar textsträngen.

# Välj sedan ut ett AK och skriv ett testfall. (red)
# Skriv sedan kod som uppfyller testfallet. (green)
# Svar: Se test/test_autocomplete_list.py
# Städa i koden, så du känner dig nöjd med din kod hittills. Fortsätt sedan med nästa AK.
