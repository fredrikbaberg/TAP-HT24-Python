# Följande kod ska sluta loopa efter 5 varv. Flytta den in i en funktion och justera den enligt kommentaren.
def upprepa(end):
    y = 1
    for x in range(1, 100):
        y *= 2
        # avsluta loopen med en if-sats här
        if x >= end:
            break
    print(y)
