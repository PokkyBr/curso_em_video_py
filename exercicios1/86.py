matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        a = int(input(f'Digite um valor para [{c},{i}]:'))
        matriz[c].append(a)

for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
print(matriz)