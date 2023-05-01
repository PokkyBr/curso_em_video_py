def aumentar(n, q, form=False):
    n = n / 100 * (100+q)
    if form:
        return moeda(n)
    return n

def diminuir(n, q, form=False):
    n = n / 100 * (100-q)
    if form:
        return moeda(n)
    return n

def dobro(n, form=False):
    if form:
        return moeda(n*2)
    return n*2

def metade(n, form=False):
    if form:
        return moeda(n/2)
    return n/2

def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')

def linha(msg):
    print('~'*40)
    print(msg.center(40))
    print('~'*40)
    
def resumo(n, aum=10, red=10):
    linha('RESUMO DO VALOR')
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{moeda(n*2)}')
    print(f'Metade do preço: \t{moeda(n/2)}')
    print(f'{aum}% de aumento: \t{moeda(aumentar(n, aum))}')
    print(f'{red}% de redução: \t{moeda(diminuir(n, red))}')
    print('~'*40)