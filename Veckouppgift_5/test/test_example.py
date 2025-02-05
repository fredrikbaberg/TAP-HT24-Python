from Veckouppgift_5.src.example import subtract

def test_subtract__subtract_correctly():
    expected = 3
    actual = subtract(10, 7)
    assert actual == expected
