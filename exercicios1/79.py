valores = []
cont = 'a'
while True:
    v = int(input('Digite um número: '))
    if v in valores:
        print('Esse número já tem na lista.')
    else:
        valores.append(v)
    while cont != 'Y' and cont != 'N':
        cont = input('Deseja continuar? [Y/N] ').upper()
#poderia usar também "while cont not in 'YyNn'"
    if cont == 'N':
        break
    cont = ''

print(sorted(valores))