from Domain.cheltuiala import getsuma, getnrapartament
from Logic.CRUD import adaugacheltuiala, getBynrapartament, stergecheltuiala
from Logic.functionalitate import adunarevaloare, ceamaimarecheltuiala, ordonaredescdupasuma, afisareasumelorlunare


def testadunarevalori():
    lista = []
    lista = adaugacheltuiala(1, 200, "10.10.2020", "canal", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "alte cheltuieli", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)

    lista = adunarevaloare(200, "10.10.2020", lista)

    assert getsuma(getBynrapartament(1, lista)) == 400
    assert getsuma(getBynrapartament(2, lista)) == 100
    assert getsuma(getBynrapartament(3, lista)) == 600


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


def testceamaimarecheltuiala():
    lista=[]
    lista = adaugacheltuiala(1, 200, "10.10.2020", "intretinere", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "alte cheltuieli", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)

    listar=[['intretinere', 400], ['canal', 0], ['alte cheltuieli', 100]]
    assert ceamaimarecheltuiala(lista)==listar

    lista = adaugacheltuiala(1, 300, "10.10.2020", "intretinere", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)
    lista = adaugacheltuiala(1, 500, "10.10.2020", "canal", lista)
    lista = adaugacheltuiala(2, 800, "11.09.2021", "alte cheltuieli", lista)
    lista = adaugacheltuiala(3, 30, "10.10.2020", "canal", lista)

    listar2=[['intretinere', 400],['canal',500],['alte cheltuieli',800]]

    assert ceamaimarecheltuiala(lista)==listar2


def testordonaredescdupasuma():
    lista=[]
    lista = adaugacheltuiala(1, 50, "10.10.2020", "canal", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)

    rezultat = ordonaredescdupasuma(lista)

    assert getnrapartament(rezultat[0]) == 3
    assert getnrapartament(rezultat[1]) == 2
    assert getnrapartament(rezultat[2]) == 1

def testafisareasumelorlunare():
    lista = []
    lista = adaugacheltuiala(1, 50, "10.10.2020", "canal", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)

    rezultat=afisareasumelorlunare(lista)

    assert len(rezultat) == 2
    assert rezultat["10"] == 450
    assert rezultat["09"] == 100













