# 4 Figurer med loopar.
# Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.

# a
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "#" if x == 1 else "."
    print(s)

print("")

# b
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "#" if x == y else "."
    print(s)

print("")

# c
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "#" if x in range(3,6) else "."
    print(s)

print("")

# d
for y in range(1,7):
    s = ""
    if y == 3:
        s += "#"*9
    else:
        for x in range(1,9):
            s += "#" if x == 3 else "."
    print(s)

print("")

# e
for y in range(1,7):
    s = ""
    for x in range(1,9):
        if y == 5:
            s += "#"
        else:
            s += "#" if y==(x-3) else "."
    print(s)

print("")