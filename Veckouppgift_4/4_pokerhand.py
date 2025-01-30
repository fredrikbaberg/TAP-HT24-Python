# När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
# poker_hand(cards)
# "Du fick ett par med valören: 5"

from pokerhand import slumpa_spelkort, poker_hand

# Skapa en hand
hand = [slumpa_spelkort.slumpa_spelkort() for _ in range(5)]

# Kontrollera handen
poker_hand.poker_hand(hand)
