from random import randint
from operator import itemgetter
lista = {}
jogadores = {}

for j in range(1, 5):
    jogadores[f'jogador{j}'] = randint(1, 6)


for j, k in jogadores.items():
    print(f'O {j} tirou {k} no dado')

lista = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for pos, p in enumerate(lista):
    print(f'posição {pos+1}: Jogador {p[0]} que tirou {p[1]} no dado.')
