lista = []
media=fem=0
pessoa = {}
while True:
    cont=' '
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    pessoa.clear()
    cont = str(input('Deseja continuar? [Y/N] ')).upper()
    if cont in 'N':
        break

for p in lista:
    media+=p['idade']
media/=len(lista)

print('-='*30)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade do grupo é de {media:.2f} anos')
print('As mulheres do grupo são: ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(p['nome'], end=' ')
print()
print('Lista com as pessoas com a idade acima da média:')
for p in lista:
    if p['idade'] > media:
        print()
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}')

print('<<  ENCERRADO  >>')