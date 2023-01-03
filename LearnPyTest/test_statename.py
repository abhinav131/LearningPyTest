def validation6(state):
    if len(state)>2 and len(state)<51:
        return True
    else:
        return False


def test1():
    assert(validation6(""))

def test2():
    assert(validation6("a"))

def test3():
    assert(validation6('sd'))

def test4():
    assert(validation6('GOA'))

def test5():
    assert(validation6('Delhi'))

def test6():
    assert(validation6('Jammu and Kashmir'))

def test7():
    assert(validation6("The State of Rhode Island and Providence Plantations"))
