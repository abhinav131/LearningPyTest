import re
import pytest

def validation4(pinCode):
    #regex = "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$"
    regex = "^[1-9]{1}[0-9]{5}$"
    p = re.compile(regex)

    if (pinCode == ''):
        return False

    m = re.match(p, pinCode)
    if m is None:
        return False
    else:
        return True

def test1():
    assert(validation4('123456'))

def test2():
    assert(validation4('103 456'))

def test3():
    assert(validation4('023456'))

def test4():
    assert(validation4('45893475'))

def test5():
    assert(validation4('273213'))

def test6():
    assert(validation4('273 213'))








