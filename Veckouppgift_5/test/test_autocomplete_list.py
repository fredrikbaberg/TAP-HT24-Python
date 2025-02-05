
from Veckouppgift_5.src.autocomplete_list import autocomplete_list

def test_autocomplete_list__empty_alternatives():
    expected = []
    assert autocomplete_list("", []) == expected

def test_autocomplete_list__empty_string():
    expected = []
    assert autocomplete_list("", ["1", "2", "3"]) == expected

def test_autocomplete_list__with_options():
    expected = ["first", "fire"]
    master_list = ["first", "fire", "second", "score"]
    assert autocomplete_list("fi", master_list) == expected
    assert autocomplete_list("se", master_list) == ["second"]
