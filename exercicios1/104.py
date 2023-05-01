def leiaint(msg):
    global n
    while True:
        n = input(msg)
        if n.isnumeric():
            break
        print('\33[0;31mERRO! Digite um número inteiro válido.\33[m')
    return n


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')