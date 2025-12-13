#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math

from tasks.sum_series import Series


def test_term():
    s = Series(x=2.0)

    assert math.isclose(s._term(0), 2.0**0 / 2**1 * 1, rel_tol=1e-9)
    assert math.isclose(s._term(1), -(2.0**1) / 2**2, rel_tol=1e-9)
    assert math.isclose(s._term(2), 2.0**2 / 2**3, rel_tol=1e-9)


def test_ex_value():
    s = Series(x=1.2)
    expected = 1 / (2 + 1.2)
    assert math.isclose(s.ex_value(), expected, rel_tol=1e-9)


def test_calculate_single_thread():
    s = Series(x=1.2, eps=1e-7)
    result = s.calculate(num_threads=1)
    expected = s.ex_value()
    assert math.isclose(result, expected, rel_tol=1e-6)


def test_calculate_multi_thread():
    s = Series(x=1.2, eps=1e-7)
    result = s.calculate(num_threads=4)
    expected = s.ex_value()
    assert math.isclose(result, expected, rel_tol=1e-6)


def test_str_method():
    s = Series(x=1.5, eps=1e-7)
    string = str(s)
    assert "Исходный ряд" in string
    assert "x = 1.5" in string
    assert "epsilon = 1e-07" in string
    assert "S = 1 / (2 + x)" in string
