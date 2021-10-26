from Domain.cheltuiala import creeazacheltuiala, getnrapartament, getsuma, getdata, gettipul


def testcheltuiala():
    cheltuiala = creeazacheltuiala(1, 250, "10.09.2021", "intretinere")

    assert getnrapartament(cheltuiala) == 1
    assert getsuma(cheltuiala) == 250
    assert getdata(cheltuiala) == "10.09.2021"
    assert gettipul(cheltuiala) == "intretinere"


