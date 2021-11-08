from datetime import datetime

from Domain.cheltuiala import toString, getsuma, gettipul, getdata, getnrapartament
from Logic.CRUD import adaugacheltuiala, stergecheltuiala, modificacheltuiala, getBynrapartament, getBydata
# from Logic.functionalitate import stergereatuturorcheltuielilor
from Logic.functionalitate import adunarevaloare, ceamaimarecheltuiala, ordonaredescdupasuma, afisareasumelorlunare


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Stergerea tuturor cheltuielilor")
    print("5. Adunarea unei valori la toate cheltuielile dintr-o dată citită")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială")
    print("7. Ordonarea cheltuielilor descrescător după sumă")
    print("8. Afișarea sumelor lunare pentru fiecare apartament")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiAdaugacheltuiala(lista, undoOperations, redoOperations):
    try:
        nrapartament = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma cheltuielii: "))
        data1 = input("Dati data cheltuielii: ")
        data = datetime.strptime(data1, '%d.%m.%Y').date().strftime("%d.%m.%Y")
        listatip = ["intretinere", "canal", "alte cheltuieli"]
        tipul = input("Dati tipul cheltuielii: ")
        if tipul not in listatip:
            raise ValueError("Nu exista acest tip de cheltuiala!")
        rezultat = adaugacheltuiala(nrapartament, suma, data, tipul, lista)
        undoOperations.append([
            lambda: stergecheltuiala(nrapartament, rezultat),
            lambda: adaugacheltuiala(nrapartament, suma, data, tipul, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
    return lista


def uiStergecheltuiala(lista, undoOperations, redoOperations):
    try:
        nrapartament = int(input("Dati nr apartamentului cheltuielii de sters: "))
        rezultat = stergecheltuiala(nrapartament, lista)
        cheltuialaDeSters = getBynrapartament(nrapartament, lista)
        undoOperations.append([
            lambda: adaugacheltuiala(
                nrapartament,
                getsuma(cheltuialaDeSters),
                getdata(cheltuialaDeSters),
                gettipul(cheltuialaDeSters),
                rezultat),
            lambda: stergecheltuiala(nrapartament, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiModificacheltuiala(lista, undoOperations, redoOperations):
    try:
        nrapartament = int(input("Dati numarul apartamentului de modificat: "))
        suma = float(input("Dati noua suma: "))
        data1 = input("Dati noua data a cheltuielii: ")
        data = datetime.strptime(data1, '%d.%m.%Y').date().strftime("%d.%m.%Y")
        tipul = input("Dati noul tip al cheltuielii: ")
        listatip = ["intretinere", "canal", "alte cheltuieli"]
        if tipul not in listatip:
            raise ValueError("Nu exista acest tip de cheltuiala!")
        rezultat = modificacheltuiala(nrapartament, suma, data, tipul, lista)
        cheltuialaVeche = getBynrapartament(nrapartament, lista)
        undoOperations.append([
            lambda: modificacheltuiala(
                nrapartament,
                getsuma(cheltuialaVeche),
                getdata(cheltuialaVeche),
                gettipul(cheltuialaVeche),
                rezultat),
            lambda: modificacheltuiala(nrapartament, suma, data, tipul, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


'''

def uistergereatuturorcheltuielilor(lista):
    nrapartament=int(input("Dati numarul apartamentului pentru stergerea totala a chetuielilor:"))
    return stergereatuturorcheltuielilor(nrapartament,lista)
'''


def uiAdunarevaloare(lista, undoOperations, redoOperations):
    try:
        data2 = input("Dati data: ")
        data = datetime.strptime(data2, '%d.%m.%Y').date().strftime("%d.%m.%Y")
        valoare = float(input("Dati valoarea de adunat:"))
        rezultat= adunarevaloare(valoare, data, lista)
        cheltuialaVeche = getBydata(data, lista)
        undoOperations.append([
            lambda: modificacheltuiala(
                getnrapartament(cheltuialaVeche),
                getsuma(cheltuialaVeche),
                data,
                gettipul(cheltuialaVeche),
                rezultat),
            lambda: adunarevaloare(valoare, data, lista)
        ])
        redoOperations.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista


def uiordonaredupasuma(lista):
    showAll(ordonaredescdupasuma(lista))


def uiafisareasumelorlunare(lista):
    rezultat = afisareasumelorlunare(lista)
    for luna in rezultat:
        print("Suma lunara pentru luna {} este de {}".format(luna, rezultat[luna]))


'''

def uireadCommandLine(lista):
    stringCommandLine = input("Dati comenzile separate prin virgula:")
    return readCommandLine(stringCommandLine,lista)
'''


def runMenu(lista):
    undoOperations = []
    redoOperations = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugacheltuiala(lista, undoOperations, redoOperations)
        elif optiune == "2":
            lista = uiStergecheltuiala(lista, undoOperations, redoOperations)
        elif optiune == "3":
            lista = uiModificacheltuiala(lista, undoOperations, redoOperations)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "4":
            lista = uiStergecheltuiala(lista, undoOperations, redoOperations)
        elif optiune == "5":
            lista = uiAdunarevaloare(lista, undoOperations, redoOperations)
        elif optiune == "6":
            lista3 = ceamaimarecheltuiala(lista)
            for i in range(len(lista3)):
                print(lista3[i][0] + ":\n")
                for cheltuiala in lista:
                    if getsuma(cheltuiala) == lista3[i][1] and gettipul(cheltuiala) == lista3[i][0]:
                        print(cheltuiala, "\n")
        elif optiune == "7":
            uiordonaredupasuma(lista)
        elif optiune == "8":
            uiafisareasumelorlunare(lista)
        elif optiune == "u":
            if len(undoOperations) > 0:
                operations = undoOperations.pop()
                redoOperations.append(operations)
                lista = operations[0]()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoOperations) > 0:
                operations = redoOperations.pop()
                undoOperations.append(operations)
                lista = operations[1]()
            else:
                print("Nu se poate face redo!")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
