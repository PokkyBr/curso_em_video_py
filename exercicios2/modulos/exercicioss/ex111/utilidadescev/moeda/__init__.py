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
    print('~'*(len(msg)+4))
    print(f'  {msg}  ')
    print('~'*(len(msg)+4))
    
def resumo(n, aum=10, red=10):
    linha('RESUMO DO VALOR')
    print(f'Preço analisado:{moeda(n):>10}')
    print(f'Dobro do preço:{moeda(n*2):>10}')
    print(f'Metade do preço:{moeda(n/2):>10}')
    print(f'{aum}% de aumento:{moeda(aumentar(n, aum)):>10}')
    print(f'{red}% de redução:{moeda(diminuir(n, red)):>10}')
    print('~'*40)