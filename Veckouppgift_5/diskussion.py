# 1a. x > 100:
# Alla tal strikt större än 100 (även flyttal).
# 1b. y == 42:
# y exakt lika med 42.
# 1c. len(text) >= 5:
# Alla strängar med längd större än eller lika med 5.
# 1d. z == True
# Om booleanen är True
# 1e. 8 < v < 16
# v skall vara mellan 8 och 16, dvs strikt mindre än 16 och över 8.
# 1f. w == 32 or w == 64 or w == 128
# Variabel nw får endast anta värdena 32, 64 eller 128.
# 1g. if x < 5: … elif x < 10: … elif x < 15: … else
# 4 ekvivalensklasser: x<5, 5<x<10, 10<x<15, resten.
x = input('Ange ett värde: ')
if x < 5:
    print("1")
elif x < 10:
    print("2")
elif x < 15:
    print("3")
else:
    print(4)



# 2.
def uppgift_2():
    # Returnerar summan av alla tal i listan
    def sum_list(list):
        return None

    def test_empty_list():
        expected = 0
        actual   = sum_list([])
        assert actual == expected
        
    def test_number_list():
        assert sum_list([5]) == 5
        assert sum_list([1,2,3,4,5]) == 15
        assert sum_list([0,0,0,0,0]) == 0
        assert sum_list([-1,-2,-3,-4,-5]) == -15
