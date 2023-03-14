from calculator import calculator
def test_shortDistance():
    """
    We test the function with a distance of 499m
    with increasing item amounts
    """
    assert calculator(499, 4, 10, 2022, 1, 31, 14, 00) == 100
    assert calculator(499, 5, 10, 2022, 1, 31, 14, 00) == 150
    assert calculator(499, 10, 10, 2022, 1, 31, 14, 00) == 400 
    assert calculator(499, 13, 10, 2022, 1, 31, 14, 00) == 670
    
    #We implement the Friday rush multiplier
    assert calculator(499, 4, 10, 2023, 2, 3, 16, 30) == 120
    assert calculator(499, 5, 10, 2023, 2, 3, 16, 30) == 180
    assert calculator(499, 10, 10, 2023, 2, 3, 16, 30) == 480
    assert calculator(499, 13, 10, 2023, 2, 3, 16, 30) == 804
 
def test_distance1000():
    """
    Test the function with a distance of 1km
    with increasing item amounts
    """
    assert calculator(1000, 4, 10, 2023, 2, 3, 14, 00) == 200
    assert calculator(1000, 5, 10, 2023, 2, 3, 14, 00) == 250
    assert calculator(1000, 10, 10, 2023, 2, 3, 14, 00) == 500
    assert calculator(1000, 13, 10, 2023, 2, 3, 14, 00) == 770

    #With Friday rush multiplier

    assert calculator(1000, 4, 10, 2023, 2, 3, 16, 30) == 240
    assert calculator(1000, 5, 10, 2023, 2, 3, 16, 30) == 300
    assert calculator(1000, 10, 10, 2023, 2, 3, 16, 30) == 600
    assert calculator(1000, 13, 10, 2023, 2, 3, 16, 30) == 924

def test_distance1500():
    """
    Test the function with a distance of 1.5km
    with increasing item amounts
    """
    assert calculator(1500, 4, 10, 2023, 2, 3, 14, 00) == 300
    assert calculator(1500, 5, 10, 2023, 2, 3, 14, 00) == 350
    assert calculator(1500, 10, 10, 2023, 2, 3, 14, 00) == 600
    assert calculator(1500, 13, 10, 2023, 2, 3, 14, 00) == 870

    #With Friday rush multiplier

    assert calculator(1500, 4, 10, 2023, 2, 3, 16, 30) == 360
    assert calculator(1500, 5, 10, 2023, 2, 3, 16, 30) == 420
    assert calculator(1500, 10, 10, 2023, 2, 3, 16, 30) == 720
    assert calculator(1500, 13, 10, 2023, 2, 3, 16, 30) == 1044

def test_distance1501():
    """
    Test the function with a distance of 1501m
    with increasing item amounts
    """
    assert calculator(1501, 4, 10, 2023, 2, 3, 14, 00) == 400
    assert calculator(1501, 5, 10, 2023, 2, 3, 14, 00) == 450
    assert calculator(1501, 10, 10, 2023, 2, 3, 14, 00) == 700
    assert calculator(1501, 13, 10, 2023, 2, 3, 14, 00) == 970


    #With Friday rush modifier

    assert calculator(1501, 4, 10, 2023, 2, 3, 16, 30) == 480
    assert calculator(1501, 5, 10, 2023, 2, 3, 16, 30) == 540
    assert calculator(1501, 10, 10, 2023, 2, 3, 16, 30) == 840
    assert calculator(1501, 13, 10, 2023, 2, 3, 16, 30) == 1164

def test_longDistance():
    """
    Test the function with a distance of 10km
    with increasing item amounts.
    """
    assert calculator(10000, 4, 10, 2023, 2, 3, 14, 00) == 1500
    assert calculator(10000, 5, 10, 2023, 2, 3, 14, 00) == 1500
    assert calculator(10000, 10, 10, 2023, 2, 3, 14, 00) == 1500
    assert calculator(10000, 13, 10, 2023, 2, 3, 14, 00) == 1500

    #With Friday rush modifier

    assert calculator(10000, 4, 10, 2023, 2, 3, 16, 30) == 1500
    assert calculator(10000, 5, 10, 2023, 2, 3, 16, 30) == 1500
    assert calculator(10000, 10, 10, 2023, 2, 3, 16, 30) == 1500
    assert calculator(10000, 13, 10, 2023, 2, 3, 16, 30) == 1500

def test_lowValue():
    """
    We test the function for a low cart value 
    with increasing distances
    """
    assert calculator(499, 4, 5.35, 2023, 2, 3, 14, 00) == 565
    assert calculator(1000, 4, 5.35, 2023, 2, 3, 14, 00) == 665
    assert calculator(1500, 4, 5.35, 2023, 2, 3, 14, 00) == 765
    assert calculator(1501, 4, 5.35, 2023, 2, 3, 14, 00) == 865
    assert calculator(10000, 4, 5.35, 2023, 2, 3, 14, 00) == 1500
    
    #With Friday rush multiplier

    assert calculator(499, 4, 5.35, 2023, 2, 3, 16, 30) == 678
    assert calculator(1000, 4, 5.35, 2023, 2, 3, 16, 30) == 798
    assert calculator(1500, 4, 5.35, 2023, 2, 3, 16, 30) == 918
    assert calculator(1501, 4, 5.35, 2023, 2, 3, 16, 30) == 1038
    assert calculator(10000, 4, 5.35, 2023, 2, 3, 16, 30) == 1500

def test_highValue():
    """
    Test the code with a high cart value
    """
    assert calculator(1000, 12, 100, 2023, 2, 3, 14, 00) == 0

def test_negativeDistance():
    """
    Test the code with a negative distance
    """
    assert calculator(-1, 4, 10, 2023, 2, 3, 14, 00) == "Error: Please enter a valid distance"