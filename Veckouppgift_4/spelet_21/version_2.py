# i stället för att använda talserien, slumpa tal mellan 1 och 13. (talen i en vanlig kortlek)
# Tips: importera modulen random och använd funktionen randint för att slumpa tal. 
# Exempel: card = random.randint(1, 13)
# 
# Möjlig vidareutveckling: bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna. (slumpa ett tal) Gör så att datorn kan simulera en motståndare. Målet är att vinna över datorn.

from random import randint

def slumpat_kort():
    sum = 0
    while True:
        if sum > 21:
            print(f"Första talet större än 21 är {sum}.")
            break
        card = randint(1, 13)
        sum += card
        print(f"Slumpade {card}, summan är: {sum}")

def blackjack():
    sum = 0
    while True:
        if sum > 21:
            print("Du passerade 21!")
            break
        dra_kort = input(f"Du är just nu på {sum}, vill du dra ett kort? (j/n)")
        if dra_kort in ['j', 'J']:
            card = randint(1, 13)
            sum += card
        else: # Ta hand om alla andra fall.
            break
    print(f"Du stannade på {sum}.")
