import pytest

def fizzbuzz(i):
    if i % 15 == 0:
        return "FizzBuzz"
    elif i % 3 == 0:
        return "Fizz"
    elif i % 5 == 0:
        return "Buzz"
    else:
        return i


def test_divisibility_by_15():
    assert fizzbuzz(30) == "FizzBuzz"

def test_divisibility_by_3():
    assert fizzbuzz(12) == "Fizz"

def test_divisibility_by_5():
    assert fizzbuzz(50) == "Buzz"

def test_other_divisibility():
    assert fizzbuzz(7) == 7 