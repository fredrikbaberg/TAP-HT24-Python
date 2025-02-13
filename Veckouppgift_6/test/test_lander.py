from Veckouppgift_6.src.lander import Country

def test__country_print_country_sweden():
    expected = "I Sverige bor det 10.5 miljoner invånare."
    actual = Country("Sverige", 10.5).__str__()
    assert expected == actual

def test__country_print_country_iceland():
    expected = "I Island bor det 0.4 miljoner invånare."
    actual = Country("Island", 0.4).__str__()
    assert expected == actual

def test__country_default_area_is_none():
    expected = None
    actual = Country("Sverige", 0.4).area
    assert expected == actual

def test__country_area_is_stored():
    expected = 1.0
    actual = Country("Sverige", 0.4, area=1.0).area
    assert expected == actual

def test__country_area_is_printed():
    expected = "I Sverige bor det 10.5 miljoner invånare. Arean är 447425 km^2"
    actual = Country("Sverige", 10.5, area=447425).__str__()
    assert expected == actual

def test__country_add_language():
    fi = Country("Finland", 10.5)
    fi.add_language("finska")
    fi.add_language("svenska")
    expected = ["finska", "svenska"]
    actual = fi.languages
    assert expected == actual

def test_country__print_languages():
    se = Country("Sverige", 10.5)
    # se.add_language("finska")
    se.add_language("svenska")
    expected = "I Sverige bor det 10.5 miljoner invånare.\nOfficiella språk är: svenska."
    actual = se.__str__()
    assert expected == actual
