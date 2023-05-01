def aumentar(n, q, form=False):
    n = n / 100 * (100+q)
    """if form:
        return moeda(n)"""
    return n if form is False else moeda(n)

def diminuir(n, q, form=False):
    n = n / 100 * (100-q)
    """if form:
        return moeda(n)"""
    return n if form is False else moeda(n)

def dobro(n, form=False):
#    if form:
#        return moeda(n*2)
    return n*2 if form is False else moeda(n*2)

def metade(n, form=False):
#    if form:
#        return moeda(n/2)
    return n/2 if form is False else moeda(n/2)

def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')