# test_jar.py

import jar
import pytest

def test_initial_capacity():
    j = jar.Jar()
    assert j.capacity == 12

def test_initial_size():
    j = jar.Jar()
    assert j.size == 0

def test_deposit():
    j = jar.Jar()
    j.deposit(5)
    assert j.size == 5

def test_withdraw():
    j = jar.Jar()
    j.deposit(5)
    j.withdraw(3)
    assert j.size == 2

def test_capacity_negative():
    with pytest.raises(ValueError):
        j = jar.Jar(-1)

def test_size_negative():
    j = jar.Jar()
    with pytest.raises(ValueError):
        j.size = -1

def test_size_exceed_capacity():
    j = jar.Jar()
    with pytest.raises(ValueError):
        j.deposit(15)

def test_str_representation():
    j = jar.Jar()
    j.deposit(3)
    assert str(j) == "***"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "test_jar.py"])
