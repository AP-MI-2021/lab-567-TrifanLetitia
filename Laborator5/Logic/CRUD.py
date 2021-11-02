from Domain.cheltuiala import creeazacheltuiala, getnrapartament, getdata, gettipul


def adaugacheltuiala(nrapartament, suma, data, tipul,lista):
    '''

    :param nrapartament: int
    :param suma: float
    :param data: date
    :param tipul: string
    :param lista: lista de cheltuieli
    :return: o lista continand atat elementele vechi, cat si noua prajitura
    '''
    cheltuiala = creeazacheltuiala(nrapartament, suma, data, tipul)
    return lista + [cheltuiala]


def getBynrapartament(nrapartament, lista):
    '''
    gaseste o cheltuiala cu numarul apartamentului dat intr-o lista
    :param nrapartament: int
    :param lista: lista de cheltuieli
    :return: cheltuiala cu nr apartamentului dat din lista sau None, daca aceasta nu exista
    '''
    for cheltuiala in lista:
        if getnrapartament(cheltuiala) == nrapartament:
            return cheltuiala
    return None

def getBytipul(tipul,lista):
    '''

    :param tipul:
    :param lista:
    :return:
    '''
    for cheltuiala in lista:
        if gettipul(cheltuiala) == tipul:
            return cheltuiala
    return None

def getBydata(data,lista):
    '''

    :param data:
    :param lista:
    :return:
    '''
    for cheltuiala in lista:
        if getdata(cheltuiala) == data:
            return cheltuiala
    return None

def stergecheltuiala(nrapartament, lista):
    '''
    sterge o cheltuiala cu numarul apartamentului dat dintr-o lista
    :param nrapartament: int
    :param lista: lista de cheltuieli
    :return: o lista de cheltuieli fara elementul cu numarul apartamentului dat
    '''
    if getBynrapartament(nrapartament, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu numarul de apartament dat!")
    return [cheltuiala for cheltuiala in lista if getnrapartament(cheltuiala) != nrapartament]



def modificacheltuiala(nrapartament, suma, data, tipul, lista):
    '''
    modifica o cheltuiala cu numarul apartamentului dat
    :param nrapartament: int
    :param suma: float
    :param data: date
    :param tipul: string
    :param lista: lista de cheltuieli
    :return: lista modificata
    '''
    if getBynrapartament(nrapartament, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu numarul de apartament dat!")
    listaNoua = []
    for cheltuiala in lista:
        if getnrapartament(cheltuiala) == nrapartament:
            cheltuialaNoua = creeazacheltuiala(nrapartament, suma, data, tipul)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua