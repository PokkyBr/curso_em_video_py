import random
numeros = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
print(numeros)
for pos, c in enumerate(numeros):
    if pos == 0:
        maior = c
        menor = c
    if maior < c:
        maior = c
    if menor > c:
        menor = c
print(f'O maior número é: {maior}\nO menor número é: {menor}')