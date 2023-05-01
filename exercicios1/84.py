pessoas = []
dados = []

i=0

while True:
    cont=' '
    dados.append(input('Digite seu nome: '))
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    i+=1
    if i == 1:
        maisp = maisl = dados[0]
        pesop = pesol = dados[1]
    else:
        if pesop < dados[1]:
            maisp = dados[0]
            pesop = dados[1]
        if pesol > dados[1]:
            maisl = dados[0]
            pesol = dados[1]
    dados.clear()
    cont = input('Deseja continuar? (Y/N)').upper()
    if cont in 'N':
        break

print(pessoas)
pl = [maisl]
pp = [maisp]

for p in pessoas:
    if p[0] != maisp:
        if p[1] == pesop:
            pp.append(p[0])
    if p[0] != maisl:
        if p[1] == pesol:
            pl.append(p[0])

print(f'Foram cadastradas {i} pessoas\nPessoas mais leves: {pl} com {pesol:.2f}kg.\nPessoas mais pesadas: {pp} com {pesop:.2f}kg.')
#dá para usar o "len(pessoas)" no lugar do i

print('Pessoas mais leves: ', end='')
for p in pessoas:
    if p[1] == pesol:
        print(f'{p[0]}.', end=' ')
print('Pessoas mais leves: ', end='')
for p in pessoas:
    if p[1] == pesop:
        print(f'{p[0]}.', end=' ')