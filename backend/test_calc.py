from calculator import calculator
def test_shortDistance():
    """
    We test the function with a distance of 499m
    with increasing item amounts
    """
    assert calculator(499, 4, 10, 2022, 1, 31, 14, 00) == 1.00
    assert calculator(499, 5, 10, 2022, 1, 31, 14, 00) == 1.50
    assert calculator(499, 10, 10, 2022, 1, 31, 14, 00) == 4.00 
    assert calculator(499, 13, 10, 2022, 1, 31, 14, 00) == 6.70
    
    #We implement the Friday rush multiplier
    assert calculator(499, 4, 10, 2023, 2, 3, 16, 30) == 1.20
    assert calculator(499, 5, 10, 2023, 2, 3, 16, 30) == 1.80
    assert calculator(499, 10, 10, 2023, 2, 3, 16, 30) == 4.80
    assert calculator(499, 13, 10, 2023, 2, 3, 16, 30) == 8.04
 
def test_distance1000():
    """
    Test the function with a distance of 1km
    with increasing item amounts
    """
    assert calculator(1000, 4, 10, 2023, 2, 3, 14, 00) == 2.00
    assert calculator(1000, 5, 10, 2023, 2, 3, 14, 00) == 2.50
    assert calculator(1000, 10, 10, 2023, 2, 3, 14, 00) == 5.00
    assert calculator(1000, 13, 10, 2023, 2, 3, 14, 00) == 7.70

    #With Friday rush multiplier

    assert calculator(1000, 4, 10, 2023, 2, 3, 16, 30) == 2.40
    assert calculator(1000, 5, 10, 2023, 2, 3, 16, 30) == 3.00
    assert calculator(1000, 10, 10, 2023, 2, 3, 16, 30) == 6.00
    assert calculator(1000, 13, 10, 2023, 2, 3, 16, 30) == 9.24

def test_distance1500():
    """
    Test the function with a distance of 1.5km
    with increasing item amounts
    """
    assert calculator(1500, 4, 10, 2023, 2, 3, 14, 00) == 3.00
    assert calculator(1500, 5, 10, 2023, 2, 3, 14, 00) == 3.50
    assert calculator(1500, 10, 10, 2023, 2, 3, 14, 00) == 6.00
    assert calculator(1500, 13, 10, 2023, 2, 3, 14, 00) == 8.70

    #With Friday rush multiplier

    assert calculator(1500, 4, 10, 2023, 2, 3, 16, 30) == 3.60
    assert calculator(1500, 5, 10, 2023, 2, 3, 16, 30) == 4.20
    assert calculator(1500, 10, 10, 2023, 2, 3, 16, 30) == 7.20
    assert calculator(1500, 13, 10, 2023, 2, 3, 16, 30) == 10.44

def test_distance1501():
    """
    Test the function with a distance of 1501m
    with increasing item amounts
    """
    assert calculator(1501, 4, 10, 2023, 2, 3, 14, 00) == 4.00
    assert calculator(1501, 5, 10, 2023, 2, 3, 14, 00) == 4.50
    assert calculator(1501, 10, 10, 2023, 2, 3, 14, 00) == 7.00
    assert calculator(1501, 13, 10, 2023, 2, 3, 14, 00) == 9.70


    #With Friday rush modifier

    assert calculator(1501, 4, 10, 2023, 2, 3, 16, 30) == 4.8
    assert calculator(1501, 5, 10, 2023, 2, 3, 16, 30) == 5.4
    assert calculator(1501, 10, 10, 2023, 2, 3, 16, 30) == 8.4
    assert calculator(1501, 13, 10, 2023, 2, 3, 16, 30) == 11.64

def test_longDistance():
    """
    Test the function with a distance of 10km
    with increasing item amounts.
    """
    assert calculator(10000, 4, 10, 2023, 2, 3, 14, 00) == 15.00
    assert calculator(10000, 5, 10, 2023, 2, 3, 14, 00) == 15.00
    assert calculator(10000, 10, 10, 2023, 2, 3, 14, 00) == 15.00
    assert calculator(10000, 13, 10, 2023, 2, 3, 14, 00) == 15.00

    #With Friday rush modifier

    assert calculator(10000, 4, 10, 2023, 2, 3, 16, 30) == 15.00
    assert calculator(10000, 5, 10, 2023, 2, 3, 16, 30) == 15.00
    assert calculator(10000, 10, 10, 2023, 2, 3, 16, 30) == 15.00
    assert calculator(10000, 13, 10, 2023, 2, 3, 16, 30) == 15.00

def test_lowValue():
    """
    We test the function for a low cart value 
    with increasing distances
    """
    assert calculator(499, 4, 5.35, 2023, 2, 3, 14, 00) == 5.65
    assert calculator(1000, 4, 5.35, 2023, 2, 3, 14, 00) == 6.65
    assert calculator(1500, 4, 5.35, 2023, 2, 3, 14, 00) == 7.65
    assert calculator(1501, 4, 5.35, 2023, 2, 3, 14, 00) == 8.65
    assert calculator(10000, 4, 5.35, 2023, 2, 3, 14, 00) == 15.00
    
    #With Friday rush multiplier

    assert calculator(499, 4, 5.35, 2023, 2, 3, 16, 30) == 6.78
    assert calculator(1000, 4, 5.35, 2023, 2, 3, 16, 30) == 7.98
    assert calculator(1500, 4, 5.35, 2023, 2, 3, 16, 30) == 9.18
    assert calculator(1501, 4, 5.35, 2023, 2, 3, 16, 30) == 10.38
    assert calculator(10000, 4, 5.35, 2023, 2, 3, 16, 30) == 15.00

def test_highValue():
    """
    Test the code with a high cart value
    """
    assert calculator(1000, 12, 100, 2023, 1, 27, 14, 00) == 0