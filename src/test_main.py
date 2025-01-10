#  NAME:  SHAKHRIZOD
#  FILE:  The main testing file
#  REQUIREMENTS:  pytest



#  Import modules
import pytest
from data_processing import process_data


#  Normal data testing
def test_process_data_normal_case():
    data = [
        {"id": 1, "value": 2},
        {"id": 2, "value": 3}]
    result = process_data(data)
    
    expected = [
        {"id": 1, "new_value": 4},
        {"id": 2, "new_value": 9}]
    assert result == expected

#  Empty list data testing
def test_process_data_empty_list():
    data = []
    result = process_data(data)
    expected = []
    assert result == expected

#  Invalid data testing
def test_process_data_invalid_structure():
    data = [
        {"id": 1, "wrong_key": 2},  # Incorrect key
        {"id": 2, "value": "abc"}]  # Invalid value
    
    with pytest.raises(KeyError):
        process_data(data)

#  Invalid type data testing
def test_process_data_invalid_type():
    data = "This is not a list!"
    with pytest.raises(TypeError):
        process_data(data)

#  Large data testing
def test_process_data_large_values():
    data = [
        {"id": 1, "value": 10 ** 6},
        {"id": 2, "value": -10 ** 6}]
    result = process_data(data)
    
    expected = [
        {"id": 1, "new_value": 10 ** 12},
        {"id": 2, "new_value": 10 ** 12}]
    assert result == expected
