from Domain.cheltuiala import getdata, creeazacheltuiala, getnrapartament, getsuma, gettipul

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
    da un dictionar cu key=tipul de cheltuiala si values=suma cheltuielii
    :param lista: lista de cheltuieli
    :return: dictionar
    '''
    listatip=["intretinere", "canal", "alte cheltuieli"]
    Dict={}
    for tip in listatip:
        Dict[tip]=[]
    for cheltuiala in lista:
        Dict[gettipul(cheltuiala)].append(getsuma(cheltuiala))
    return Dict




















