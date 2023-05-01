lista1=[]
lista2=[]
lista3=[]

while True:
    cont=' '
    n = int(input('Digite um número: '))
    lista1.append(n)
    while cont not in 'YN':
        cont = input('Deseja continuar? (Y/N) ').upper()
    if cont in 'N':
        break

for num in lista1:
    if num % 2==0:
        lista2.append(num)
    else:
        lista3.append(num)

print('lista 1:', lista1)
print('lista 2:', lista2)
print('lista 3:', lista3)