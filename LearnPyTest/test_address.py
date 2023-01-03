def validation5(billing_address):
    if len(billing_address)>4 and len(billing_address)<201:
        return True
    else:
        return False

def test1():
    assert(validation5(""))

def test2():
    assert(validation5("q"))

def test3():
    assert(validation5("qe"))

def test4():
    assert(validation5("dfg"))

def test5():
    assert(validation5("rtyu"))

def test6():
    assert(validation5("df-47"))

def test7():
    assert(validation5("hu/480"))

def test8():
    assert(validation5("24/9 ,Mohan Cooperative Industrial Estate, Mathura Road, AWFIS , South East Delhi"))

def test9():
    assert(validation5("qwe                       23fft/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////..."))