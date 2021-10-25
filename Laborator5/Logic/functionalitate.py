from Domain.cheltuiala import getdata, creeazacheltuiala, getnrapartament, gettipul, getsuma


def adunarevaloare(valoare,data1,lista):
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























