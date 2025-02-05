from Veckouppgift_5.src.multiplication_table import multiplication_table

def test_multiplication_table__limit_0():
    expected = []
    actual = multiplication_table(n=0, limit=0)
    assert actual == expected

def test_multiplication_table__n_and_limit():
    expected = [3, 6, 9, 12]
    actual = multiplication_table(n=3, limit=4)
    assert actual == expected
