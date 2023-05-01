a1 = int(input('Digite o primeiro termo da razão PA: '))
r = int(input('Digite a razão do termo PA: '))
n=a=1
while n < 11:
    an = a1 + (n-1)*r
    print(f'O termo de número {n} é {an}.')
    n+=1

while a != 0:
    a = int(input('Digite o numero de termos que voce quer mostrar a mais e 0 para finalizar o pro programa encerrar: '))
    b = n+a
    if a != 0:
        while b > n:    
            an = a1 + (n-1)*r
            print(f'O termo de número {n} é {an}.')
            n+=1