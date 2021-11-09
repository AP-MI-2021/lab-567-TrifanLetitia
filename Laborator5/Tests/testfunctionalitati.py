from Domain.cheltuiala import getsuma, getnrapartament
from Logic.CRUD import adaugacheltuiala, getBynrapartament, stergecheltuiala
from Logic.functionalitate import adunarevaloare, ceamaimarecheltuiala, ordonaredescdupasuma, afisareasumelorlunare, \
    UNDO, REDO


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


def testUNDO():
    lista = []
    lista = adaugacheltuiala(1, 50, "10.10.2020", "canal", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)

    undoOperations=[]
    redoOperations = []
    undoOperations.append([
        lambda: stergecheltuiala(3, lista),
        lambda: adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)
    ])
    redoOperations.clear()

    lista=UNDO(lista, undoOperations , redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'},
                    {'nrapartament': 2, 'suma': 100, 'data': '11.09.2021', 'tipul': 'intretinere'}]

    undoOperations.append([
        lambda: stergecheltuiala(2, lista),
        lambda: adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    ])
    redoOperations.clear()

    lista = UNDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'}]

    undoOperations.append([
        lambda: stergecheltuiala(1, lista),
        lambda: adaugacheltuiala(1, 50, "10.10.2020", "canal", lista)
    ])
    redoOperations.clear()

    lista = UNDO(lista, undoOperations, redoOperations)
    assert lista == []

    lista= UNDO(lista, undoOperations, redoOperations)
    assert lista == []

    lista = []
    lista = adaugacheltuiala(1, 50, "10.10.2020", "canal", lista)
    lista = adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)

    undoOperations=[]
    redoOperations=[]

    lista=REDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'},
                     {'nrapartament': 2, 'suma': 100, 'data': '11.09.2021', 'tipul': 'intretinere'},
                     {'nrapartament': 3, 'suma': 400, 'data': '10.10.2020', 'tipul': 'intretinere'}]

    undoOperations = []
    redoOperations = []
    undoOperations.append([
        lambda: stergecheltuiala(3, lista),
        lambda: adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)
    ])
    redoOperations.clear()

    lista = UNDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'},
                     {'nrapartament': 2, 'suma': 100, 'data': '11.09.2021', 'tipul': 'intretinere'}]

    undoOperations.append([
        lambda: stergecheltuiala(2, lista),
        lambda: adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    ])
    redoOperations.clear()

    lista = UNDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'}]

    redoOperations.append([
        lambda: stergecheltuiala(2, lista),
        lambda: adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    ])

    lista=REDO(lista, undoOperations, redoOperations)
    assert lista== [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'},
                    {'nrapartament': 2, 'suma': 100, 'data': '11.09.2021', 'tipul': 'intretinere'}]

    redoOperations.append([
        lambda: stergecheltuiala(3, lista),
        lambda: adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)
    ])

    lista=REDO(lista, undoOperations, redoOperations)
    assert lista==[{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'},
                   {'nrapartament': 2, 'suma': 100, 'data': '11.09.2021', 'tipul': 'intretinere'},
                   {'nrapartament': 3, 'suma': 400, 'data': '10.10.2020', 'tipul': 'intretinere'}]

    undoOperations.append([
        lambda: stergecheltuiala(3, lista),
        lambda: adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)
    ])
    redoOperations.clear()

    undoOperations = []
    redoOperations = []
    undoOperations.append([
        lambda: stergecheltuiala(3, lista),
        lambda: adaugacheltuiala(3, 400, "10.10.2020", "intretinere", lista)
    ])
    redoOperations.clear()

    lista = UNDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'},
                     {'nrapartament': 2, 'suma': 100, 'data': '11.09.2021', 'tipul': 'intretinere'}]

    undoOperations.append([
        lambda: stergecheltuiala(2, lista),
        lambda: adaugacheltuiala(2, 100, "11.09.2021", "intretinere", lista)
    ])
    redoOperations.clear()

    lista = UNDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'}]

    lista=adaugacheltuiala(4,150,"10.10.2020","canal",lista)

    undoOperations.append([
        lambda: stergecheltuiala(4, lista),
        lambda: adaugacheltuiala(4,150,"10.10.2020","canal",lista)
    ])
    redoOperations.clear()
    lista=UNDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'}]

    undoOperations.append([
        lambda: stergecheltuiala(1, lista),
        lambda: adaugacheltuiala(1, 50, "10.10.2020", "canal", lista)
    ])
    redoOperations.clear()
    lista=UNDO(lista, undoOperations, redoOperations)
    assert lista== []

    redoOperations.append([
        lambda: stergecheltuiala(1, lista),
        lambda: adaugacheltuiala(1, 50, "10.10.2020", "canal", lista)
    ])
    lista=REDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'}]

    redoOperations.append([
        lambda: stergecheltuiala(4, lista),
        lambda: adaugacheltuiala(4,150,"10.10.2020","canal",lista)
    ])
    lista = REDO(lista, undoOperations, redoOperations)
    assert lista == [{'nrapartament': 1, 'suma': 50, 'data': '10.10.2020', 'tipul': 'canal'},
                     {'nrapartament': 4, 'suma': 150, 'data': '10.10.2020', 'tipul': 'canal'}]


























































