valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = valores[c]
        posmaior = c
        menor = valores[c]
        posmenor = c
    if valores[c] > maior:
        maior = valores[c]
        posmaior = c
    if valores[c] < menor:
        menor = valores[c]
        posmenor = c

print(f'O menor valor foi {menor} na posição {posmenor} e o maior valor foi {maior} na posição {posmaior}.')
print(valores)