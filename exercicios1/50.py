i=0
for c in range(0,6):
    n1 = int(input('Digite um número: '))
    if n1 % 2 == 0:
        i += n1
print(f'A soma dos números (pares) é: {i}')