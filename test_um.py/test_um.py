import pytest
from um import count

def test_count_correct():
    assert count("um") == 1
    assert count("um, hello") == 1
    assert count("Um, hello um.") == 2
    assert count("Um... I'm not sure.") == 1
    assert count("Yummy food.") == 0
    assert count("Um, um, um") == 3
    assert count("Some random text") == 0
    assert count("The word um is quite common.") == 1
    assert count("I heard you say um quite a few times.") == 1
    assert count("Umm, not sure what you mean.") == 0  # 'Umm' is not 'um'
    assert count("He likes to hum.") == 0  # 'hum' is not 'um'

def test_count_incorrect_word():
    assert count("dumb and dumber") == 0  # 'dumber' contains 'um'
    assert count("Plum is a fruit") == 0  # 'Plum' contains 'um'
    assert count("I'm numb") == 0  # 'numb' contains 'um'
    assert count("Umbrella is useful") == 0  # 'Umbrella' contains 'um'

def test_count_incorrect_spacing():
    assert count("hummingbird") == 0  # 'hum' is not surrounded by spaces
    assert count("column") == 0  # 'um' is not surrounded by spaces
    assert count("album") == 0  # 'um' is not surrounded by spaces
    assert count("lumberjack") == 0  # 'um' is not surrounded by spaces

if __name__ == "__main__":
    pytest.main()
