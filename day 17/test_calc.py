
import pytest
from calc import add, divide, Calculator

# Test individual functions
def test_add_positive():
    assert add(2, 3) == 5  
def test_add_negative():
    assert add(-1, 1) == 0

def test_add_zero():
    assert add(0, 5) == 5

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_divide_zero_error():
    with pytest.raises(ValueError):  
        divide(10, 0)

# Test class methods
def test_calculator_multiply():
    calc = Calculator()
    result = calc.multiply(4, 5)
    assert result == 20  


