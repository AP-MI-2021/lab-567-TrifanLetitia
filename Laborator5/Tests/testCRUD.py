from Domain import cheltuiala
from Domain.cheltuiala import getnrapartament, getsuma, getdata, gettipul
from Logic.CRUD import adaugacheltuiala, getBynrapartament, stergecheltuiala, modificacheltuiala, getBydata


def testAdaugacheltuiala():
    lista = []
    lista = adaugacheltuiala(1, 250, "10.09.2021" ,"intretinere",lista)

    assert len(lista) == 1
    assert getnrapartament(getBynrapartament(1, lista)) == 1
    assert getsuma(getBynrapartament(1, lista)) == 250
    assert getdata(getBynrapartament(1, lista)) == "10.09.2021"
    assert gettipul(getBynrapartament(1, lista)) == "intretinere"

def testStergecheltuiala():
    lista = []
    lista = adaugacheltuiala(1, 250, "10.09.2021", "intretinere",lista)
    lista = adaugacheltuiala(2, 350, "11.09.2021", "canal" , lista)

    lista = stergecheltuiala(1, lista)

    assert len(lista) == 1
    assert getBynrapartament(1, lista) is None
    assert getBynrapartament(2, lista) is not None

    lista = stergecheltuiala(3, lista)

    assert len(lista) == 1
    assert getBynrapartament(2, lista) is not None

def testModificacheltuiala():
    lista = []
    lista = adaugacheltuiala(1, 250, "10.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(2, 350, "11.09.2021","canal",lista)

    lista = modificacheltuiala(1, 400, "9.10.2021", "alte cheltuieli", lista)

    cheltuialaUpdatata = getBynrapartament(1, lista)
    assert getnrapartament(cheltuialaUpdatata) == 1
    assert getsuma(cheltuialaUpdatata) == 400
    assert getdata(cheltuialaUpdatata) == "9.10.2021"
    assert gettipul(cheltuialaUpdatata) == "alte cheltuieli"

    cheltuialaNeupdatata = getBynrapartament(2, lista)
    assert getnrapartament(cheltuialaNeupdatata) == 2
    assert getsuma(cheltuialaNeupdatata) == 350
    assert getdata(cheltuialaNeupdatata) == "11.09.2021"
    assert gettipul(cheltuialaNeupdatata) == "canal"

    lista = []
    lista = adaugacheltuiala(1, 250, "10.09.2021", "intretinere", lista)

    lista = modificacheltuiala(3, 400, "9.10.2021", "alte cheltuieli", lista)

    cheltuialaNeupdatata = getBynrapartament(1, lista)
    assert getnrapartament(cheltuialaNeupdatata) == 1
    assert getsuma(cheltuialaNeupdatata) == 250
    assert getdata(cheltuialaNeupdatata) == "10.09.2021"
    assert gettipul(cheltuialaNeupdatata) == "intretinere"

def testgetByData():
    lista=[]
    lista=adaugacheltuiala(1, 250,"10.09.2021" ,"intretinere",lista)
    assert getBydata("12.03.2021",lista)==None

def testgetBynrapartament():
       lista = []
       lista = adaugacheltuiala(1, 250, "10.09.2021", "intretinere", lista)
       assert getBynrapartament(1,lista) == [('nrapartament', 1), ('suma', 250), ('data', '10.09.2021'), ('tipul', 'intretinere')]


