import pytest
from math_operations.math_operations import add, subtract


# Fixture to set up some common data for the tests
@pytest.fixture
def common_data():
    return {'x': 10, 'y': 5}


# Test the add function
def test_add(common_data):
    result = add(common_data['x'], common_data['y'])
    assert result == 15
    
    
# Test the subtract function
def test_subtract(common_data):
    result = subtract(common_data['x'], common_data['y'])
    assert result == 5
    
    
# Test the multiply method of the Calculator class
def test_calculator_multiply(calculator_instance, common_data):
    result = calculator_instance.multiply(common_data['x'], common_data['y'])
    assert result == 50
    
    
# Test the divide method of the Calculator class
def test_calculator_divide(calculator_instance, common_data):
    result = calculator_instance.divide(common_data['x'], common_data['y'])
    assert result == 2.0
    
    
# Test division by zero using a marker
@pytest.mark.divide_by_zero
def test_calculator_divide_by_zero(calculator_instance, common_data):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator_instance.divide(common_data['x'], 0)
        
        
# Use marks to categorize tests
@pytest.mark.parametrize("input_x, input_y, expected_result", [(2, 3, 5), (0, 0, 0), (-2, -3, -5)])
def test_add_parametrized(input_x, input_y, expected_result):
    result = add(input_x, input_y)
    assert result == expected_result
