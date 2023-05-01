import time
def maior(*num):
    if len(num) > 0:
        print(f'Os números digitados foram:')
        for pos, n in enumerate(num):
            print(n, end=' ', flush=True)
            time.sleep(0.5)
            if pos == 0:
                maior = n
            if n > maior:
                maior = n
        print(f'Ao todo foram informados {len(num)} valores.')
        print(f'O maior número é o {maior}.')
        print('-='*30)
    else:
        print('foram informados 0 valores ao todo.')
        print('O maior valor informado foi 0.')

maior(2,4,3,5,7,8,5,4,34,545,65,63,4,34,34,23,43,42,4,5,452,4)
maior()