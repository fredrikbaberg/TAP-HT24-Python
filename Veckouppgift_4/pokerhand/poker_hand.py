# Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.

from pokerhand.jamfor_spelkort import har_lika_valor
from pokerhand.konstanter import valor_till_text

# Skriv ut kortet på ett snyggare sätt.
pretty_print_card = lambda kort: print(f"{kort[0]} {valor_till_text[kort[1]]}")

def poker_hand(hand):
    print(f"Kollar handen: {hand}")
    # Sortera handen efter valör
    hand_sorterad = sorted(hand, key=lambda x: x[1])

    # Leta efter par
    for i in range(len(hand_sorterad)-1):
        lika = har_lika_valor(hand_sorterad[i], hand_sorterad[i+1])
        if lika:
            print(f"Hittade par: {hand[i]}, {hand[i+1]}.")

# Testa poker_hand med olika kombinationer.
def test_poker_hand():
    # Skriv ut kort
    pretty_print_card(['hjärter', 12])
    # Ett par
    resultat = poker_hand([['hjärter', 2], ['klöver', 2], ['ruter', 2]])
    # assert resultat == "par i 2"


if __name__=='__main__':
    print("Testa poker_hand.")
    test_poker_hand()
