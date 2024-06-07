
import working
import pytest

def test_convert_valid_12_hour_format():
    assert working.convert("11:30 AM to 3:45 PM") == "11:30 to 15:45"

def test_convert_valid_12_hour_format_no_minutes():
    assert working.convert("1 PM to 3 AM") == "13:00 to 03:00"

def test_convert_valid_12_hour_format_edge_cases():
    assert working.convert("12:15 AM to 12:30 PM") == "00:15 to 12:30"
    assert working.convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_convert_invalid_format():
    with pytest.raises(ValueError):
        working.convert("Invalid time format")

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "test_working.py"])
