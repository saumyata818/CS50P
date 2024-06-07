
import seasons
from datetime import date
import pytest

def test_days_diff():
    start_date = date(2023, 1, 1)
    end_date = date(2023, 1, 2)
    assert seasons.days_diff(start_date, end_date) == 1440  # 1440 minutes in a day

def test_validate_date_valid():
    assert seasons.validate_date("2023-01-01") == date(2023, 1, 1)

def test_validate_date_invalid():
    assert seasons.validate_date("invalid_date") == False

def test_number_to_word():
    assert seasons.number_to_word(5) == "five"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "test_seasons.py"])
