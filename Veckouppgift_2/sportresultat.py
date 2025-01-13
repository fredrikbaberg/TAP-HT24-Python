print("Matchen är över, nu ska vi räkna ut resultatet!")
in_tottenham = input("Hur många mål gjorde Tottenham? ")
in_liverpool = input("Hur många mål gjorde Liverpool? ")

score_tottenham = int(in_tottenham)
score_liverpool = int(in_liverpool)
score_difference = abs(score_tottenham-score_liverpool)

if(score_tottenham > score_liverpool):
    print("Tottenham vann med {} mål!".format(score_difference))
elif(score_liverpool > score_tottenham):
    print("Liverpool vann med {} mål!".format(score_difference))
else:
    print("Oavgjort")
