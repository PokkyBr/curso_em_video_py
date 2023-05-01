lista = []
i=0
while True:
    cont='a'
    n = int(input('Digite um número: '))
    lista.append(n)
    while cont not in 'YN':
        cont = input('Deseja continuar? (Y/N)').upper()
    if cont in 'N':
        break
    i+=1

print(f'Foram digitados {i} números')
print(f'Foram digitados os valores na ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')