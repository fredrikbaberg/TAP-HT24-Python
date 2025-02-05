from Veckouppgift_5.src.uppgift_2_1 import c_to_f

def test_c_to_f__low_returns_none():
    expected = None
    actual = c_to_f(-273.16)
    assert expected == actual
