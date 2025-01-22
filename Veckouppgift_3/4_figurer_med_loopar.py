# 4 Figurer med loopar.
# Skriv in följande kod och modifiera den, så att den skriver ut figurerna a-j en i taget.

# a
print("a)")
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "#" if x == 1 else "."
    print(s)

# b
print("\nb)")
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "#" if x == y else "."
    print(s)

# c
print("\nc)")
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "#" if x in range(3,6) else "."
    print(s)

# d
print("\nd)")
for y in range(1,7):
    s = ""
    if y == 3:
        s += "#"*8
    else:
        for x in range(1,9):
            s += "#" if x == 3 else "."
    print(s)

# e
print("\ne)")
for y in range(1,7):
    s = ""
    for x in range(1,9):
        if x == 5:
            s += "#"
        else:
            s += "#" if x==(7-y) else "."
    print(s)

# f
print("\nf)")
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "#" if x==(y) or x==(7-y) else '.'
    print(s)

# g
print("\ng)")
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += "." if x%2==0 else "#"
    print(s)

# h
print("\nh)")
for y in range(1,7):
    s = ""
    if y in [1,6]:
        s += "."*8
    elif y in [2,5]:
        s += f".{'#'*6}."
    elif y in [3,4]:
        s += f".#{'.'*4}#."
    print(s)

# i
print("\ni)")
sTemplate = ".#0"*3
for y in range(1,7):
    s = ""
    for x in range(1,9):
        s += sTemplate[(x-y)%3]
    print(s)

# j
print("\nj)")
for y in range(1,7):
    s = ""
    for x in range(1,9):
        if y in [1,2,3]:
            s += "#" if x%3 == 0 else "."
        elif y in [5,6]:
            s += "." if (x+y)%2==0 else "#"
        else:
            s += '.'
    print(s)
