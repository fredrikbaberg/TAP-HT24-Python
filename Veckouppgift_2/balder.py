height = input("Hur lång är du (cm)? ")
min_height = 130

if(int(height) >= min_height):
    print("Du får åka!")
else:
    print("Du får inte åka")


# Fråga: Varför tre värden?
# Svar: Finns tre olika fall att testa:
#     * Under gränsen
#     * På gränsen
#     * Över gränsen
# 129 cm behövs inte, eftersom det inte finns någon koll för det.