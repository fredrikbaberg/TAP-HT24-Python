# 1a Det är ca 470 km mellan Stockholm och Göteborg. Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg. Du behöver fråga användaren hur fort man ska köra, i km/h.
hastighet = input("Hur fort ska du köra (km/h)? ")
tid = 470/int(hastighet)
print("Det tar {:.2f} timmar".format(tid))
print("Det tar {} minuter".format(str(tid*60)))

# 1b Gör så att programmet svarar i minuter i stället för sekunder.
print("Det tar {} sekunder".format(str(tid*60*60)))

'''
1c (svårare) Nu ska programmet svara i hela timmar och minuter.
Tips: använd operatorerna // och %. Heltalsdivision // dividerar och avrundar nedåt till närmaste heltal. Procent % räknar ut resten vid division med heltal. Exempel:
3 // 2 == 1      (3 / 2 == 1.5, avrundar nedåt)
60 % 60 == 0  (ingen rest)
70 % 60 == 10  (10 i rest)
Be en AI förklara heltalsdivision och modulo i Python om du känner dig osäker!
'''
tid_i_sekunder = tid*3600
timmar = tid_i_sekunder // 3600
minuter = (tid_i_sekunder % 3600) // 60
sekunder = (tid_i_sekunder % 3600) % 60
print("Det tar {} timmar, {} minuter och {} sekunder".format(str(timmar), str(minuter), str(sekunder) ))
