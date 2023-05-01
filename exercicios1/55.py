i=0
j=999999
for c in range(0, 5):
    peso = float(input('Digite o seu peso: '))
    if peso > i:
        i = peso
    if peso < j:
        j = peso

print(f'O maior peso é {i:.1f} e o menor peso é {j:.1f}.')