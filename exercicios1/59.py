c=0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

while c!=5:
    c = int(input('1-somar\n2-multiplicar\n3-maior\n4-novos numeros\n5-sair do programa\nDigite a opção desejada: '))
    if c == 1:
        print(f'A soma de {n1} com {n2} é igual a {n1+n2}')
    elif c == 2:
        print(f'A multiplicação de {n1} com {n2} é igual a {n1*n2}')
    elif c == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}.')
        else:
            print(f'{n1} e {n2} são iguais.')
    elif c == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
print('FIM')