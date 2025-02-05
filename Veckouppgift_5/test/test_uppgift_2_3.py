
from Veckouppgift_5.src.uppgift_2_3 import find_median


def test_find_median__median_number():
    expected = 2
    assert find_median([1,2,3]) == expected

def test_find_median__even_number_of_elements():
    expected = 2.5
    assert find_median([1,2,3,4]) == expected
