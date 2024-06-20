import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("0/4") == 0
    assert convert("2/4") == 50
    assert convert("4/4") == 100
    with pytest.raises(ValueError):
        convert("4/2")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"

