from Domain.cheltuiala import toString, getsuma, gettipul
from Logic.CRUD import adaugacheltuiala, stergecheltuiala, modificacheltuiala
# from Logic.functionalitate import stergereatuturorcheltuielilor
from Logic.functionalitate import adunarevaloare, ceamaimarecheltuiala


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala")
    print("3. Modificare cheltuiala")
    print("4. Stergerea tuturor cheltuielilor")
    print("5. Adunarea unei valori la toate cheltuielile dintr-o dată citită")
    print("6. Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuială")
    print("a. Afisare cheltuieli")
    print("x. Iesire")


def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiAdaugacheltuiala(lista):
    nrapartament = int(input("Dati numarul apartamentului: "))
    suma = float(input("Dati suma cheltuielii: "))
    data = input("Dati data cheltuielii: ")
    tipul = input("Dati tipul cheltuielii: ")
    return adaugacheltuiala(nrapartament, suma, data, tipul, lista)


def uiStergecheltuiala(lista):
    nrapartament = int(input("Dati nr apartamentului cheltuielii de sters: "))
    return stergecheltuiala(nrapartament, lista)


def uiModificacheltuiala(lista):
    nrapartament = int(input("Dati numarul apartamentului de modificat: "))
    suma = float(input("Dati noua suma: "))
    data = input("Dati noua data a cheltuielii: ")
    tipul = input("Dati noul tip al cheltuielii: ")
    return modificacheltuiala(nrapartament, suma, data, tipul)


'''

def uistergereatuturorcheltuielilor(lista):
    nrapartament=int(input("Dati numarul apartamentului pentru stergerea totala a chetuielilor:"))
    return stergereatuturorcheltuielilor(nrapartament,lista)
'''


def uiAdunarevaloare(lista):
    data1 = input("Dati data:")
    valoare = float(input("Dati valoarea de adunat:"))
    return adunarevaloare(valoare, data1, lista)



def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugacheltuiala(lista)
        elif optiune == "2":
            lista = uiStergecheltuiala(lista)
        elif optiune == "3":
            lista = uiModificacheltuiala(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "4":
            lista = uiStergecheltuiala(lista)
        elif optiune == "5":
            lista = uiAdunarevaloare(lista)
        elif optiune == "6":
            lista3=ceamaimarecheltuiala(lista)
            for i in range(len(lista3)):
                print(lista3[i][0]+":\n")
                for cheltuiala in lista:
                    if getsuma(cheltuiala)== lista3[i][1] and gettipul(cheltuiala)==lista3[i][0]:
                        print(cheltuiala,"\n")
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
