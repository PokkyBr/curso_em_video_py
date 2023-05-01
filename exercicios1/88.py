import random, time
jogos = int(input('Quantos jogos serão? '))
lista = []
a = []
for c in range(0, jogos):
    for j in range(0, 6):
        a.append(random.randint(1, 60))
    print(f'Jogo {c+1}: {sorted(a)}')
    a.clear()
    if c != jogos-1:
        time.sleep(1)

print(f'{"fim":=^20}')