
from Veckouppgift_5.src.balansera_listor import balansera_listor


def test_balansera_listor__lika_langd():
    expected = ([1,2], [3, 4])
    assert balansera_listor([1,2], [3,4]) == expected

def test_balansera_listor__skillnad_max_1():
    expected = ([1,2,3], [4,5])
    assert balansera_listor([1, 2, 3], [4, 5]) == expected

def test_balansera_listor__alla_i_ena_jamnt():
    expected = ([1, 2], [3, 4])
    actual1, actual2 = balansera_listor([1, 2, 3, 4], [])
    # Ordningen spelar ingen roll, sortera listorna före jämförelse.
    actual1.sort()
    actual2.sort()
    assert (actual1, actual2) == expected

def test_balansera_listor__alla_i_ena_udda():
    expected = ([1, 2, 3, 4], [5, 6, 7])
    actual1, actual2 = balansera_listor([1, 2, 3, 4, 5, 6 ,7], [])
    # Ordningen spelar ingen roll, sortera listorna före jämförelse.
    actual1.sort()
    actual2.sort()
    assert (actual1, actual2) == expected