from Logic.CRUD import adaugacheltuiala
from Logic.functionalitate import ceamaimarecheltuiala
from Tests.testAll import runAllTests
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugacheltuiala(1, 250, "01.09.2021" , "intretinere", lista)
    lista = adaugacheltuiala(2, 250, "01.09.2021", "canal", lista)
    lista = adaugacheltuiala(3, 200, "01.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(4, 400, "01.09.2021", "canal", lista)

    runMenu(lista)

main()