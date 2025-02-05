from Veckouppgift_5.src.uppgift_2_4 import is_sorted_ascending


def test_is_sorted_ascending__not_sorted():
    expected = False
    assert is_sorted_ascending([3,2,1]) == expected

def test_is_sorted_ascending__sorted():
    expected = True
    assert is_sorted_ascending([1, 4, 5]) == True
