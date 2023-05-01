import random
numeros = []

def sorteio(lista):
    print('Números sorteados: ', end='')
    for i in range(0, 5):
        lista.append(random.randint(1, 100))
        print(f'{lista[i]}', end=' ')
    print('FIM!')
        

def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma+=n
    print(f'Somando os valores pares de {numeros}, temos {soma}')
    

sorteio(numeros)
somaPar(numeros)