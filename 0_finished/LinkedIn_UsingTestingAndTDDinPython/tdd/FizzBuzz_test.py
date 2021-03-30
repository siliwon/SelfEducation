import pytest


def fizz_buzz(value):
    if is_multiple(value, 15):
        return "FizzBuzz"
    if is_multiple(value, 3):
        return 'Fizz'
    if is_multiple(value, 5):
        return 'Buzz'
    return str(value)

def is_multiple(value, mod):
    return (value % mod) == 0

def check_fizz_buzz(value, expected_ret_val):
    assert expected_ret_val == fizz_buzz(value)


def test_returns_with_1_passed_in():
    check_fizz_buzz(1, "1")


def test_returns_with_2_passed_in():
    check_fizz_buzz(2, "2")


def test_returns_fizz_with_3_passed_in():
    check_fizz_buzz(3, 'Fizz')


def test_returns_buzz_with_5_passed_in():
    check_fizz_buzz(5, 'Buzz')


def test_returns_fizz_with_6_passed_in():
    check_fizz_buzz(6, 'Fizz')


def test_returns_buzz_with_10_passed_in():
    check_fizz_buzz(10, 'Buzz')

def test_returns_fizzbuzz_with_15_passed_in():
    check_fizz_buzz(15, 'FizzBuzz')
