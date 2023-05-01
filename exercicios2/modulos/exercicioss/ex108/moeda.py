def aumentar(n, q):
    n = n / 100 * (100+q)
    return n

def diminuir(n, q):
    n = n / 100 * (100-q)
    return n

def dobro(n):
    return n*2

def metade(n):
    return n/2

def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')