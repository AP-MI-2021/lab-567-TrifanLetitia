from Logic.CRUD import adaugacheltuiala
from Tests.testAll import runAllTests
from UI.commandLine_console import runConsole
from UI.console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugacheltuiala(1, 250, "01.09.2021" , "intretinere", lista)
    lista = adaugacheltuiala(2, 250, "01.09.2021", "canal", lista)
    lista = adaugacheltuiala(3, 200, "01.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(4, 400, "01.09.2021", "canal", lista)
    lista = adaugacheltuiala(4, 250, "01.09.2021", "intretinere", lista)



    runMenu(lista)

    lista = []
    lista = adaugacheltuiala(1, 250, "01.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(2, 250, "01.09.2021", "canal", lista)
    lista = adaugacheltuiala(3, 200, "01.09.2021", "intretinere", lista)
    lista = adaugacheltuiala(4, 400, "01.09.2021", "canal", lista)
    lista = adaugacheltuiala(4, 250, "01.09.2021", "intretinere", lista)
    runConsole(lista)


main()


