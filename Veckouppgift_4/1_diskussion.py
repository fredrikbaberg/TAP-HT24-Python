# 1a.
gissning_1a = "1a. Gissning: Kommer skriva ut 'test'."
print(gissning_1a)
try:
    def foo(t):
        print("test")
    foo("hej")
except:
    print("Misslyckades")

# 1b.
gissning_1b = "1b. Gissning: Kommer skriva ut 3, 5"
print(gissning_1b)
try:
    def fun1(x, y):
        return x * y
    print(3, 5)
except:
    print("Misslyckades")

# 1c
gissning_1c = "1c. Gissning: Kommer skriva ut 15."
print(gissning_1c)
try:
    def fun1(x, y):
        return x * y
    print(fun1(3, 5))
except:
    print("Misslyckades")

# 1d
gissning_1d = "1d. Gissning: Kommer skriva ut 125 ( 5*(5*2+5*3) )"
print(gissning_1d)
try:
    def fun2(i):
        return 5 * i

    x = 2
    y = 3
    a = fun2(fun2(x) + fun2(y))
    print(a)
except:
    print("Misslyckades")

# 1e
gissning_1e = "1e. Gissning: Kommer skriva ut 7."
print(gissning_1e)
try:
    a = 5
    def fun3(a):
        a += 1

    a += 2
    print(a)
except:
    print("Misslyckades")

# 1f.
gissning_1f = "1f. Gissning: Kommer krascha p.g.a. semikolon."
print(gissning_1f)
try:
    def foo(i):
        return 2*i*i

    def goo(x, y):
        return x(y)

    a = goo(foo, 3);
    print(a)
except:
    print("Misslyckades")

# 1g.
gissning_1g = "1g. Gissning: Returnerar True om typen för argumentet är flyttal eller heltal, annars False."
print(gissning_1g)
try:
    def is_number(x):
        if isinstance(x, int):
            return True
        elif isinstance(x, float):
            return True
        return False
    
    print(is_number(5.5))
    print(is_number(42))
except:
    print("Misslyckades")

# 1h.
gissning_1h = "1h. Gissning: Skickar tillbaka en lista med ord som är 5-7 tecken långa."
print(gissning_1h)
try:
    def average_words(strings):
        found = []
        for item in strings:
            if 4 < len(item) < 8:
                found.append(item)
        return found
    
    average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])
except:
    print("Misslyckades")

# 1i.
gissning_1i = [
    "1i.",
    "\t 1. Gissning: Hitta minsta talet i en lista.",
    "\t 2. Gissning: Förväntat resultat: '-11', '' (kommer vara 0), '100' (kommer vara 0)"
    "\t 3. Gissning: Byt 'counter = 0' till 'counter = numbers[0] if len(numbers) > 0 else None"
]
print('\n'.join(gissning_1i))
try:
    def find_min(numbers):
        counter = 0
        for item in numbers:
            if item < counter:
                counter = item
        print(f"The smallest item is: {counter}")
        return counter
    find_min([10, 3, -4, -111])
    find_min([])
    find_min([100])
except:
    print("Misslyckades")