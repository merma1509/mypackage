from mypackage import myModule

def test_top_n():
    """
    Make sure top-n function works correctly and properly
    """
    
    assert myModule.top_n([1, 2, 4, 5, 6], 3) ==  [5, 6, 4],  "Incorrect output"
    assert myModule.top_n([1, 2, 4, 5, 6],  2) ==  [5, 6],   "Incorrect output"
    assert myModule.top_n([1, 2, 4, 5, 6, 7, 8], 6) == [8, 7, 6, 5, 4, 2],  "Incorrect output"