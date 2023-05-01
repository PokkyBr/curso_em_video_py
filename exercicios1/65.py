y = 'Y'
i=b=0
while y == 'Y':
    a = int(input('Digite um número: '))
    y = input('quer continuar? (Y/N) ').upper()
    if i == 0:
        maior = a
        menor = a
    if a > maior:
        maior = a
    elif a < menor:
        menor = a
    b = a + b
    i+=1
print(f'A média é igual a {b/i}, o maior é {maior} e o menor é {menor}.')