#  Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

def har_lika_valor(kort1, kort2):
    if kort1[1] == kort2[1]:
        if kort1[0] == kort2[0]:
            print("  Nu gick något fel, samma kort förekommer två gånger!")
            # raise ValueError('Samma kort ska inte förekomma två gånger.')
        return True
    return False

# Jämför två spelkort. Med index kan elementet som ska jämföras anges.
def jamfor_kort(kort1, kort2, index=1):
    if kort1[index] == kort2[index]:
        return True
    return False

def test_har_lika_valor():
    print("Kör tester för att se om två kort har lika valör.")
    # Förbered några par att jämföra.
    hander = [
        [ ['hjärter', 1], ['klöver', 1], ],
        [ ['spader', 2], ['ruter', 3] ],
        [ ['hjärter', 14], ['hjärter', 14]],
        [ ['ruter', 5], ['klöver', 7]],
    ]
    for hand in hander:
        print(f"Korten {hand[0]} och {hand[1]} är {'lika' if har_lika_valor(hand[0], hand[1]) else 'inte lika'}.")

def test_jamfor_kort():
    hander = [
        [ ['hjärter', 1], ['klöver', 1], ],
        [ ['spader', 2], ['ruter', 3] ],
        [ ['hjärter', 14], ['hjärter', 14]],
        [ ['ruter', 5], ['klöver', 7]],
    ]
    for hand in hander:
        print(f"Korten {hand[0]} och {hand[1]} har {'lika' if jamfor_kort(hand[0], hand[1], 0) else 'inte lika'} färg.")


if __name__=='__main__':
    test_har_lika_valor()
    test_jamfor_kort()
