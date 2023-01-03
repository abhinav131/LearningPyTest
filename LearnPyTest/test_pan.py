import re
import pytest
import json

def Valid_Pan_Details(PanNo):
    regex = "[A-Z]{5}[0-9]{4}[A-Z]{1}"
    p = re.compile(regex)

    if (PanNo == None):
        return False

    if (re.search(p, PanNo) and
            len(PanNo) == 10):
        return True
    else:
        return False
    #assert(True)

# assert PanNo == Valid_Pan_Details

# test1 = "BBHUA2318J654"
# assert(Valid_Pan_Details(test1) == True)
def test1():
    assert(Valid_Pan_Details('BBHUA2318J')==True)

# str2 = "23ZAWMN69J"
# print(Valid_Pan_Details(str2))
def test2():
    assert(Valid_Pan_Details("23ZAWMN69J"))
# str3 = "BNZAA2318JM"
# print(Valid_Pan_Details(str3))
def test3():
    assert(Valid_Pan_Details("BNZAA2318JM"))
# str4 = "POSDR56734"
# print(Valid_Pan_Details(str4))
def test4():
    assert(Valid_Pan_Details("POSDR56734")==True)
# str5 = "RTU AP12345"
# print(Valid_Pan_Details(str5))
def test5():
    assert(Valid_Pan_Details("RTU AP12345")==True)





