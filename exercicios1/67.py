i=0
while True:
    n = int(input('Digite um número: (número negativo para ser interrompido o programa) '))
    if n < 0:
        break
    while i < 10:
        i+=1
        print(f'{n} x {i} = {n*i}')
    i=0
print('FIM')