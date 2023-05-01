n = int(input('Digite um número: '))
i=0
a=b=1


if n > 2:
    print(1)
    n-=1
    while i < n:
        print(f'{a}')
        a = a+b
        b = a-b
        i+=1

elif n == 1 or n == 2:
    print(1)