a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))

for c in range(1, 11):
    a = a1 + (c-1) * r
    print(f'termo {c}: {a}')