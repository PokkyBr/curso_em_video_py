matriz = [[], [], []]
pares=soma=0
for c in range(0, 3):
    for i in range(0, 3):
        a = int(input(f'Digite um valor para [{c},{i}]:'))
        matriz[c].append(a)

for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares+=matriz[l][c]
        if c == 2:
            soma+=matriz[l][c]
        if c == 0 and l == 1:
            maior=matriz[l][c]
        elif l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]

print(f'A soma dos números pares é igual a: {pares}\nA soma dos valores da terceira coluna é igual a {soma}\nO maior da segunda linha é "{maior}"')