is_member = False
level1 = 100
level2 = 300
discount = 0

price = input("Välkommen, köp något dyrt: ")
price = float(price)

if is_member:
    if price < level1:
        print("Du får ingen rabatt.")
    elif level2 > price > level1:
        print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
        discount = discount+10
    elif price >= level2:
        print("Grattis! Du har avancerat till nivå 2 och får 25% rabatt.")
        discount = discount + 25
else:
    print("Du är inte medlem.")

final_price = price * (100-discount)/100
print("Efter rabatter blir priset...." + str(final_price))
