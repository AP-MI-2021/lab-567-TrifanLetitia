from datetime import datetime
from Domain.cheltuiala import toString
from Logic.CRUD import adaugacheltuiala, stergecheltuiala, modificacheltuiala
from UI.console import runMenu


def printMENU():
    print("1. Accesati interfata veche")
    print("2. Accesati interfata noua")

def runMENU(lista):
    while True:
        printMENU()
        optiune = input("Alegeti interfata: ")

        if optiune == "1":
            runMenu(lista)
        elif optiune == "2":
            runConsole(lista)
        elif optiune == "X":
            break
        else:
            print("Optiune gresita! Reincercati: ")


def printMenuconsole():
    print("C. Comenzi(Comenzile se separa prin virgule fara spatii.)")
    print("A. Afisare")
    print("I. Iesire")

def uireadCommandLine(lista):
    stringCommandLine = input("Dati comenzile separate prin virgula:")
    return readCommandLine(stringCommandLine,lista)


def runConsole(lista):
    while True:
        printMenuconsole()
        optiune = input("Dati optiunea: ")
        if optiune == "C":
            lista = uireadCommandLine(lista)
        elif optiune == "A":
            showAllCommand(lista)


def readCommandLine(stringCommandLine, lista):
    list = stringCommandLine.split(",")
    for i in range(len(list)):
        if list[i] == "add":
            try:
                nrapartament = int(list[i + 1])
                suma = float(list[i + 2])
                data1 = list[i + 3]
                data = datetime.strptime(data1, '%d.%m.%Y').date().strftime("%d.%m.%Y")
                #data = list[i + 3]
                tipul = list[i + 4]
                listatip = ["intretinere", "canal", "alte cheltuieli"]
                if tipul not in listatip:
                    raise ValueError("Nu exista acest tip de cheltuiala!")
                lista = adaugacheltuiala(nrapartament, suma, data, tipul, lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            print("Adaugarea s a realizat cu succes")
            i = i + 4
        elif list[i] == "delete":
            try:
               nrapartament = int(list[i + 1])
               lista = stergecheltuiala(nrapartament, lista)
            except ValueError as ve:
              print("Eroare: {}".format(ve))
            print("Stergerea s-a realizat cu succes")
            i = i + 1
        elif list[i] == "update":
            try:
               nrapartament = int(list[i + 1])
               suma = float(list[i + 2])
               data = list[i + 3]
               tipul = list[i + 4]
               listatip = ["intretinere", "canal", "alte cheltuieli"]
               if tipul not in listatip:
                    raise ValueError("Nu exista acest tip de cheltuiala!")
               lista = modificacheltuiala(nrapartament, suma, data, tipul, lista)
            except ValueError as ve:
                print("Eroare: {}".format(ve))
            print("Modificarea s-a realizat cu succes")
            i = i + 4
        elif list[i] == "showall":
            showAllCommand(lista)

    return lista


def showAllCommand(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))
