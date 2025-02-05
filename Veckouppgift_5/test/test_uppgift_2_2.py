### Uppgift 2.2, count_words
from Veckouppgift_5.src.uppgift_2_2 import count_words


def test_count_words__empty():
    expected = 0
    assert count_words("") == expected

def test_count_words__not_a_string():
    expected = 0
    assert count_words(0) == expected
    assert count_words(0.0) == expected
    assert count_words(None) == expected

def test_count_words__two_words():
    expected = 2
    assert count_words("två ord") == expected

def test_count_words__five_words():
    expected = 5
    assert count_words("det här är fem ord") == expected
