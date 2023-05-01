jogador = {}
gols= []
total=0
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input('Quantas partidas jogadas: '))

for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
    total += gols[c]
print('=-'*30)
jogador['gols'] = gols.copy()
jogador['total'] = total

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for pos, gol in enumerate(gols):
    print(f'    => Na partida {pos}, fez {gol} gols.')
print(f'Foi um total de {jogador["total"]} gols.')