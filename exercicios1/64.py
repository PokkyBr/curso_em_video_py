a=b=i=0
while a != 999:
    a = int(input('Diite um número (999 para parar): '))
    if a != 999:
        b = a+b
        i+=1
print(f'A soma de todos é {b} e foram digitados no total {i} números (desconsiderando o 999).')