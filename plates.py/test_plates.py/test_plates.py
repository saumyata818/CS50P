
from plates import is_valid


def test_bounds():
    assert is_valid("C") == False
    assert is_valid("CS") == True
    assert is_valid("MoreThanSixCharacters") == False


def test_special_chars():
    assert is_valid("???") == False
    assert is_valid(" CS50 ") == False
    assert is_valid("PI3.14") == False


def test_numbers_placement():
    assert is_valid("50CS") == False
    assert is_valid("123456") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
