from Domain import cheltuiala
from Domain.cheltuiala import getdata, creeazacheltuiala, getnrapartament, gettipul, getsuma


def adunarevaloare(valoare,data1,lista):
    '''
    aduna o valoare la toate cheltuielile dintr-o data citita
    :param valoare: float
    :param data1: date
    :param lista: lista de cheltuieli
    :return: lista in care cheltuielile care contin data citita s-au modificat
    '''
    if valoare < 0:
        raise ValueError("Valoarea care se aduna trebuie sa fie pozitiva!")
    listaNoua=[]
    for cheltuiala in lista:
        if data1==getdata(cheltuiala):
            cheltuialaNoua=creeazacheltuiala(
                getnrapartament(cheltuiala),
                getsuma(cheltuiala)+valoare,
                getdata(cheltuiala),
                gettipul(cheltuiala),

            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua

def ceamaimarecheltuiala(lista):
    '''
    determina cea mai mare cheltuiala dintr o lista dupa tipul de cheltuiala
    :param lista: lista de cheltuieli
    :return: lista
    '''
    listatip=["intretinere", "canal", "alte cheltuieli"]
    Dict={}
    for tip in listatip:
        Dict[tip]=[]
    for cheltuiala in lista:
        Dict[gettipul(cheltuiala)].append(getsuma(cheltuiala))
    Lista1=[]
    for key, value in Dict.items():
        temp = [key, max(value, default=0)]
        Lista1.append(temp)
    return Lista1

def ordonaredescdupasuma(lista):
    '''
    ordoneaza descrecator cheltuielile dupa suma cheltuielii
    :param lista: lista de cheltuieli
    :return: lista ordonata descrescator
    '''
    return sorted(lista, key=getsuma , reverse=True)


def afisareasumelorlunare(lista):
    '''
    determina sumele lunare
    :param lista: lista de cheltuieli
    :return: luna si suma cheltuielilor din luna respectiva
    '''

    rezultat={}
    for cheltuiala in lista:
        luna = getdata(cheltuiala).split(".")[1]
        suma=getsuma(cheltuiala)
        if luna in rezultat:
            rezultat[luna] = rezultat[luna] + suma
        else:
            rezultat[luna] = suma
    return rezultat


def UNDO(lista, undoOperations, redoOperations):
    if len(undoOperations) > 0:
        operations = undoOperations.pop()
        redoOperations.append(operations)
        lista = operations[0]()
    else:
        return []
    return lista


def REDO(lista, undoOperations , redoOperations):
    if len(redoOperations) > 0:
        operations = redoOperations.pop()
        undoOperations.append(operations)
        lista = operations[1]()
    else:
        return lista
    return lista

























