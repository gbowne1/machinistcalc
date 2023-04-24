import pytest
from machinistcalc.app.speedfeed import calculate_speed, calculate_feed

def test_calculate_speed():
    result = calculate_speed(1000, 2)
    expected = 500
    assert result == expected

def test_calculate_feed():
    result = calculate_feed(1000, 2)
    expected = 2000
    assert result == expected