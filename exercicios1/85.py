valores =[[], []]
for c in range(0, 7):
    a = int(input('Digite um número: '))
    if a % 2 == 0:
        valores[0].append(a)
    else:
        valores[1].append(a)

print(f'Os valores pares digitados foram: {valores[0]}\nOs valores ímpares digitados foram: {valores[1]}')
