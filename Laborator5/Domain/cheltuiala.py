def creeazacheltuiala(nrapartament, suma, data, tipul):
    '''
    creaza un dictiionar ce reprezinta o cheltuiala
    :param nrapartament: int
    :param suma: float
    :param data: date
    :param tipul: string
    :return:
    '''

    return {
        "nrapartament": nrapartament,
        "suma": suma,
        "data": data,
        "tipul": tipul
    }

'''
    l1=[]
    for i in Dict:
        tpl = (i, Dict[i])
        l1.append(tpl)
    return l1
'''



def getnrapartament(cheltuiala):
    '''
    da numarul unui apartamet
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: numarul apartamentului
    '''
    #return cheltuiala[0][1]
    return cheltuiala["nrapartament"]


def getsuma(cheltuiala):
    '''
    da suma cheltuielii
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: suma (float)
    '''
    #return cheltuiala[1][1]
    return cheltuiala["suma"]


def getdata(cheltuiala):
    '''
    da data unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: data (string)
    '''
    #return cheltuiala[2][1]
    return cheltuiala["data"]


def gettipul(cheltuiala):
    '''
    da tipul unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: tipul cheltuielii (string)
    '''
    #return cheltuiala[3][1]
    return cheltuiala["tipul"]


def toString(cheltuiala):
    return "Nrapartament: {}, Suma: {}, Data: {}, Tipul: {}".format(
        getnrapartament(cheltuiala),
        getsuma(cheltuiala),
        getdata(cheltuiala),
        gettipul(cheltuiala)
    )
