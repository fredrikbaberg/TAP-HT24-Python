# Om man lägger ihop talen 1 + 2 + 3 + 4 + …  så kommer talens summa att bli större och större. Förr eller senare kommer man förbi 21. Skriv en funktion som skriver ut det första talet i talserien som är större än 21.
def forsta_storre_an_21():
    i = 1
    while True:
        if i > 21:
            print(f"Första talet större än 21 är: {i}")
            break
        print(i)
        i += (i+1)
