import pytest
from app.lathecalc import calculate_sfpm, calculate_feed, calculate_speed

def test_calculate_speed():
    result = calculate_speed(1000, 2)
    expected = 500
    assert result == expected

def test_calculate_feed():
    result = calculate_feed(1000, 2)
    expected = 2000
    assert result == expected
