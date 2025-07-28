from app import min_cars_needed
from validation import validate_inputs
import pytest

def test_function_returns_correct_value():
    assert min_cars_needed([1, 4, 1], [1, 5, 1]) == 2
    assert min_cars_needed([4, 4, 2, 4], [5, 5, 2, 5]) == 3
    assert min_cars_needed([2, 3, 4, 2], [2, 5, 7, 2]) == 2

def test_function_handles_exact_amout_of_seats():
    assert min_cars_needed([1, 2], [3]) == 1  
    assert min_cars_needed([5], [5]) == 1  
    assert min_cars_needed([10], [5, 5]) == 2

def test_function_handles_empty_lists():
    assert min_cars_needed([], []) == 0
    with pytest.raises(ValueError, match="There are not enough cars to seat the entire group"):
        min_cars_needed([1, 2], [])
    assert min_cars_needed([], [1, 2]) == 0

def test_function_handles_no_people():
    assert min_cars_needed([0, 0, 0], [1, 2, 3]) == 0
    assert min_cars_needed([0], [5]) == 0
    assert min_cars_needed([], []) == 0

def test_function_handles_no_seats():
    with pytest.raises(ValueError, match="There are not enough cars to seat the entire group"):
        min_cars_needed([1], [0])
    with pytest.raises(ValueError, match="There are not enough cars to seat the entire group"):
        min_cars_needed([5, 0], [0])
    with pytest.raises(ValueError, match="There are not enough cars to seat the entire group"):
        min_cars_needed([1, 2, 3], [])

def test_function_handles_no_people_or_seats():
    assert min_cars_needed([], []) == 0
    assert min_cars_needed([0, 0], [0, 0]) == 0 

def test_function_handles_single_car():
    assert min_cars_needed([1], [1]) == 1
    assert min_cars_needed([2], [3]) == 1
    assert min_cars_needed([0], [5]) == 0

def test_function_handles_multiple_cars_with_same_seats():
    assert min_cars_needed([1, 2], [2, 2]) == 2
    assert min_cars_needed([3, 3], [3, 3]) == 2
    assert min_cars_needed([0, 0], [1, 1]) == 0

def test_function_handles_large_numbers():
    assert min_cars_needed([1000, 2000], [3000, 4000]) == 1
    assert min_cars_needed([10000], [5000, 5000]) == 2
    with pytest.raises(ValueError, match="There are not enough cars to seat the entire group"):
        min_cars_needed([5000, 5000, 5000], [10000])

def test_function_handles_neagtive_numbers():   
    with pytest.raises(ValueError, match="Seat count cannot be negative"):
        min_cars_needed([1, 2], [-3])
    with pytest.raises(ValueError, match="People count cannot be negative"):
        min_cars_needed([-1, -2], [3])
    with pytest.raises(ValueError, match="People count cannot be negative"):
        min_cars_needed([-1, -2], [-3])

def test_function_handles_string_input():
    with pytest.raises(TypeError, match="All values in P must be integers"):
        min_cars_needed("not a list", [1, 2, 3])
    with pytest.raises(TypeError, match="All values in S must be integers"):
        min_cars_needed([1, 2, 3], "not a list")
    with pytest.raises(TypeError, match="All values in P must be integers"):
        min_cars_needed([1, 2, "three"], [1, 2, 3])
    with pytest.raises(TypeError, match="All values in S must be integers"):
        min_cars_needed([1, 2, 3], [1, 2, "three"])

def test_function_handles_floats():
    with pytest.raises(TypeError, match="All values in P must be integers"):
        min_cars_needed([1.5, 2], [3])
    with pytest.raises(TypeError, match="All values in S must be integers"):
        min_cars_needed([1, 2], [3.5])
    with pytest.raises(TypeError, match="All values in P must be integers"):
        min_cars_needed([1.0, 2], [3])
    with pytest.raises(TypeError, match="All values in S must be integers"):
        min_cars_needed([1, 2], [3.0])

def test_function_handles_boolean_values():
    with pytest.raises(TypeError, match="All values in P must be integers"):
        min_cars_needed([1, 2, True], [1, 2, 3])  
    with pytest.raises(TypeError, match="All values in S must be integers"):
        min_cars_needed([1, 2, 3], [False])  