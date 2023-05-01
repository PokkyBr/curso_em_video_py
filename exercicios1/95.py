lista = []
gols = []
jogadores = {}
while True:
    cont = ' '
    jogadores['nome'] = str(input('Nome do jogador: '))
    jogadores['partidas'] = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for c in range(0, jogadores['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    jogadores['gols'] = gols.copy()
    jogadores['total'] = sum(gols)
    gols.clear()
    lista.append(jogadores.copy())
    while cont not in 'YN':
        cont = input('Deseja continuar? [Y/N] ').upper()[0]
    if cont in 'N':
        break

print(lista)
print('-='*30)
print(f'cod ', end='')
for k in jogadores.keys():
    print(f'{k:<15}', end='')
print()
print('-'*40)
for pos, jog in enumerate(lista):
    print(f'{pos:>3} ', end='')
    for d in jog.values():
        print(f'{str(d):<15}', end='')
    print()
#    print(f'{pos:>4} {jog["nome"]:>2} {str(jog["gols"]):>10} {jog["total"]:>15}')
print('-'*40)

while True:
    busca = int(input('Digite o código de quem você quer ver os dados: (999 para cancelar) '))
    if busca == 999:
        break
    if busca >= len(lista):
        print('Não existe')
    else:
        print(f'Informações do jogador {lista[busca]["nome"]}:')
        for i, g in enumerate(lista[busca]["gols"]):
            print(f'Partida {i+1}: {g} gols.')
    print('-'*40)
