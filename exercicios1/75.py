valores = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), 
print(valores)
a = 0,
print(f'O valor 9 apareceu {valores.count(9)} vezes')

'''if valores.count(3) == 0:
    print('Não há número 3 na tupla.')
else:
    print(f'O primeiro número três foi digitado primeiramente na posição de número {valores.index(3)+1}.')'''

if 3 in valores:
    print(f'O primeiro número três foi digitado primeiramente na posição de número {valores.index(3)+1}.')
else:
    print('Não há número 3 na tupla.')

print('Os valores pares são: ', end='')
for v in valores:
    if v % 2 ==0:
        print(v, end=', ')