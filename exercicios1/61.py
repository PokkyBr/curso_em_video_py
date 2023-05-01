a1 = int(input('Digite o primeiro termo da razão PA: '))
r = int(input('Digite a razão do termo PA: '))
n=1
while n < 11:
    an = a1 + (n-1)*r
    print(f'O termo de número {n} é {an}.')
    n+=1