pris_jacka = 2000
rea = 50/100
print("Att betala: " + str(pris_jacka*(1-rea)))

rea_in = input("Ange rea i % (utan suffix): ")
print("Att betala: " + str(pris_jacka*(1-int(rea_in)/100)))
