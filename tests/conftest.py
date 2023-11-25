import pytest
from math_operations.math_operations import Calculator


# Fixture to create an instance of the Calculator class for testing
@pytest.fixture
def calculator_instance():
    return Calculator()
