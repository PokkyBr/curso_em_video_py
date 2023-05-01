def leiaint(msg):
    while True:
        try:
            inte = int(input(msg))
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não digitar')
            return 0
        except:
            print(f'\33[0;31mErro: por favor, digite um número inteiro válido.\33[m')
        else:
            return inte

def leiafloat(msg):
    while True:
        try:
            floa = float(input(msg))
        except KeyboardInterrupt:
            print(f'\nO usuário preferiu não digitar')
            return 0
        except:
            print(f'\33[0;31mErro: por favor, digite um número real válido.\33[m')
        else:
            return floa

n1 = leiaint('Digite um Inteiro: ')
n2 = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')