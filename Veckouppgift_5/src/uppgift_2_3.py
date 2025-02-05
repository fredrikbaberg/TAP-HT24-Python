# 3a Betrakta funktionen find_median(numbers), som tar en lista med tal och returnerar medianen. Median är det mittersta talet, t.ex. är medianen 2 för listan [1, 2, 1000]. Om listan har jämnt antal element ska funktionen returnera medelvärdet av de två mittersta talen. Formulera de krav och acceptanskriterier (AK) som ska gälla för funktionen.
# Svar:
# * Returnera mittersta talet i listan.
# * Returnera medelvärde av de två mittersta talen om listan har jämnt antal element.

# 3b Skriv testfall som testar alla AK.
# Svar: Se ../test/test_uppgift_2_3.py

# 3c Implementera funktionen, så att alla testfall blir gröna.

def find_median(numbers):
    number_of_elements = len(numbers)
    if number_of_elements%2 == 0:
        middle_element_left = int(number_of_elements/2-0.5)
        middle_element_right = int(number_of_elements/2+0.5)
        sum_of_middle = numbers[middle_element_left]+numbers[middle_element_right]
        return sum_of_middle/2

    return numbers[int(number_of_elements/2)]
