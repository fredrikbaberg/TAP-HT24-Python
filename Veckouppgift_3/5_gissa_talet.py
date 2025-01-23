import random

# Slumpa ett hemligt tal
secret = random.randint(1,100)

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")
antalGissningar = 0
while True:
    gissning = int(input("Gissa: "))
    antalGissningar += 1
    if gissning == secret:
        print(f"Det är rätt!! Du gjorde det på {antalGissningar} gissningar.")
        break
    elif gissning < secret:
        print("Nej, det är för lågt!")
    else:
        print("Nej, det är för högt!")
    # Version 2
    if abs(gissning-secret) <= 5:
        print("Nu börjar det brännas!")
