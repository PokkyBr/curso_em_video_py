import time

ini = time.time()
valor = int(input('Qual será o valor a ser sacado? '))
a=b=c=d=0
while True:
    while valor >= 50:
        a+=1
        valor-=50
    while valor >= 20:
        b+=1
        valor-=20
    while valor >= 10:
        c+=1
        valor-=10
    while valor >= 1:
        d+=1
        valor-=1
    if valor == 0:
        break

print(f'Serão entregues {a} cédulas de R$50;\n {b} de R$20;\n {c} de R$10;\n {d} de R$1.')

fim = time.time()
print(f'{fim-ini} seg')
'''
ini = time.time()

print(f'{"":=^40}')
print(f'{"BANCO SAFADÃO":^40}')
print(f'{"":=^40}')

valor = int(input('Digite o valor de saque: R$'))
cc = cv = cd = cu = 0
while True:
    if valor >= 50:
        valor -= 50
        cc += 1
    elif 20 <= valor <= 50:
        valor -= 20
        cv += 1
    elif 10 <= valor <= 50:
        valor -= 10
        cd += 1
    elif 1 <= valor <= 50:
        valor -= 1
        cu += 1
    else:
        break

if cc > 0:
    print(f'Total de {cc} cédula(s) de R$50')
if cv > 0:
    print(f'Total de {cv} cédula(s) de R$20')
if cd > 0:
    print(f'Total de {cd} cédula(s) de R$10')
if cu > 0:
    print(f'Total de {cu} cédula(s) de R$1')
print(f'{"":=^40}')

fim = time.time()
print(f'{fim-ini} seg')'''