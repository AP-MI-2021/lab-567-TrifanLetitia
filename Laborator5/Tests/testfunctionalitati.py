from Domain.cheltuiala import getsuma
from Logic.CRUD import adaugacheltuiala, getBynrapartament
from Logic.functionalitate import adunarevaloare, ceamaimarecheltuiala


def testadunarevalori():
    lista = []
    lista = adaugacheltuiala(1, 200, "10.10.2020", "canal", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "alte cheltuieli", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)

    lista = adunarevaloare(200, "10.10.2020", lista)

    assert getsuma(getBynrapartament(1, lista)) == 400
    assert getsuma(getBynrapartament(2, lista)) == 100
    assert getsuma(getBynrapartament(3, lista)) == 600




