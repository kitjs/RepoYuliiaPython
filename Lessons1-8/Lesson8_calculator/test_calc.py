import pytest
import culc_func as c

def test_plus_posit():
    assert c.plus(4,3)==7


def test_minus_posit():
    assert c.minus(4,3)==1

def test_mult_posit():
    assert c.mult(4,3)==12


def test_div_posit():
    assert c.div(8,2)==4

