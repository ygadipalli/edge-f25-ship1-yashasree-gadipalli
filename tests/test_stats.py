from src.ship1.stats import mean_length

def test_mean_length_basic():
    items = ["abc", "abcd", "a"]
    m = mean_length(items)
    # lengths = [3,4,1] -> mean = 8/3 = 2.666...
    assert 2.6 < m < 2.7

def test_mean_length_empty():
    items = []
    m = mean_length(items)
    assert m == 0.0
