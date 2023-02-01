from calculator import calculator
def test_min():
    assert calculator(1000, 4, 10, 2022, 1, 31, 15, 00) == 2

def test_max():
    assert calculator(10000, 13, 99, 2022, 1, 31, 15, 00) == 15

def test_lowValue():
    assert calculator(100, 1, 1, 2022, 1, 31, 15, 00) == 10

def test_highValue():
    assert calculator(1000, 12, 100, 2023, 1, 27, 15, 00) == 0

def test_rushIsTrue():
    assert calculator(1000, 4, 10, 2022, 1, 27, 16, 00) == None

#def test_lowValueRush():

#ef test_highValueRush():