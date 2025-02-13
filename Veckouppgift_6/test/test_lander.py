from Veckouppgift_6.src.lander import Country

def test__country_print_country_sweden():
    # Skriver ut information om Sverige.
    expected = "I Sverige bor det 10.5 miljoner invånare."
    actual = Country("Sverige", 10.5).__str__()
    assert expected == actual

def test__country_print_country_iceland():
    # Skriver ut information om Island.
    expected = "I Island bor det 0.4 miljoner invånare."
    actual = Country("Island", 0.4).__str__()
    assert expected == actual

def test__country_default_area_is_none():
    # Area är None om den inte är satt.
    expected = None
    actual = Country("Sverige", 0.4).area
    assert expected == actual

def test__country_area_is_stored():
    # Area har värde om det är satt.
    expected = 1.0
    actual = Country("Sverige", 0.4, area=1.0).area
    assert expected == actual

def test__country_area_is_printed():
    # Skriver ut area om den är satt.
    expected = "I Sverige bor det 10.5 miljoner invånare. Arean är 447425 km^2"
    actual = Country("Sverige", 10.5, area=447425).__str__()
    assert expected == actual

def test__country_add_language():
    # Kan lägga till flera språk.
    fi = Country("Finland", 10.5)
    fi.add_language("finska")
    fi.add_language("svenska")
    expected = ["finska", "svenska"]
    actual = fi.languages
    assert expected == actual

def test_country__print_languages():
    # Skriver ut språk(en) som lagts till.
    se = Country("Sverige", 10.5)
    se.add_language("svenska")
    se.add_language("finska") # För test.
    expected = "I Sverige bor det 10.5 miljoner invånare.\nOfficiella språk är: svenska, finska."
    actual = se.__str__()
    assert expected == actual
