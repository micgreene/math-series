import pytest

from math_series.series import fibonacci, lucas, sum_series

def test_one_fib():
  actual = fibonacci(1)
  expected = 0
  assert actual == expected

def test_two_fib():
  actual = fibonacci(2)
  expected = 1
  assert actual == expected

def test_ten_fib():
  actual = fibonacci(10)
  expected = 34
  assert actual == expected

def test_not_ten_fib():
  actual = fibonacci(10)
  expected = 1000
  assert actual != expected

def test_one_lucas():
  actual = lucas(1)
  expected = 2
  assert actual == expected

def test_two_lucas():
  actual = lucas(2)
  expected = 1
  assert actual == expected

def test_ten_lucas():
  actual = lucas(10)
  expected = 76
  assert actual == expected

def test_not_ten_lucas():
  actual = lucas(10)
  expected = 1000
  assert actual != expected

def test_one_default_sum():
  actual = sum_series(1)
  expected = 0
  assert actual == expected

def test_two_default_sum():
  actual = sum_series(2)
  expected = 1
  assert actual == expected

def test_ten_default_sum():
  actual = sum_series(10)
  expected = 34
  assert actual == expected

def test_not_ten_default_sum():
  actual = sum_series(10)
  expected = 1000
  assert actual != expected

def test_one_custom_sum():
  custom_val1 = 5
  custom_val2 = 9
  actual = sum_series(1, custom_val1, custom_val2)
  expected = 5
  assert actual == expected

def test_two_custom_sum():
  custom_val1 = 5
  custom_val2 = 9
  actual = sum_series(2, custom_val1, custom_val2)
  expected = 9
  assert actual == expected

def test_ten_custom_sum():
  custom_val1 = 5
  custom_val2 = 9
  actual = sum_series(10, custom_val1, custom_val2)
  expected = 411
  assert actual == expected

def test_not_ten_custom_sum():
  custom_val1 = 5
  custom_val2 = 9
  actual = sum_series(10, custom_val1, custom_val2)
  expected = 1000
  assert actual != expected
