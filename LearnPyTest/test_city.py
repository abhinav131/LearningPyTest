import pytest




# def validation1(request):

#     # city_name = City.get()
#     # if City.get() == "":
#     #     assert False

#     # elif len(City.get())<3:
#     #     assert False
#     city = request.GET.get("city")
#     assert len(city)>2

def validation1(city):
    if len(city) > 2 :
        return True
    else:
        False


# test1 = "Jaipur"
# assert (validation1(test1) == True)
def test1():
    assert (validation1('Jaipur') == True)


# test2 = "te"
# assert (validation1(test2) == True)
def test2():
    assert (validation1('te') == True)


# test3 = ""
# assert (validation1(test3) == True)
def test3():
    assert (validation1('') == True)


def test4():
    assert (validation1(
        'Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu') == True)


def test5():
    assert (validation1('Q') == True)

def test6():
    assert(validation1('qwe')==True)














