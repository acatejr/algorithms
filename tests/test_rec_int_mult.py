import pytest

from algorithm.main import rec_int_mult

def test_init_rec_int_mult():
    assert rec_int_mult is not None

def test_base_case_rec_int_mult():
    prod = rec_int_mult(100, 200)
    assert prod is None

def test_single_input():
    x = 1
    y = 1
    prod = rec_int_mult(x, y)
    assert prod == x * y

    x = 2
    y = 1
    prod = rec_int_mult(x, y)
    assert prod == x * y

    x = 4
    y = 0
    prod = rec_int_mult(x, y)
    assert prod == x * y

def test_double_digit_input():
    x = 10
    y = 10
    prod = rec_int_mult(x, y)
    assert prod == x * y

    x = 50
    y = 10
    prod = rec_int_mult(x, y)
    assert prod == x * y

    x = 40
    y = 90
    prod = rec_int_mult(x, y)
    assert prod == x * y


def test_quadruple_digit_input():
    x = 1000
    y = 1000
    prod = rec_int_mult(x, y)
    assert prod == x * y

    # x = 50
    # y = 10
    # prod = rec_int_mult(x, y)
    # assert prod == x * y

    # x = 40
    # y = 90
    # prod = rec_int_mult(x, y)
    # assert prod == x * y
