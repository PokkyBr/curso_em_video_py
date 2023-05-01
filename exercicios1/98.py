from time import sleep

def contador(inic, fim, passo):
    if passo < 0:
        passo = passo*-1
    if passo == 0:
        passo = 1
    if inic < fim:
        while inic <= fim:
            print(inic, end=' ', flush=True)
            inic += passo
            sleep(0.5)
        print('FIM!')
    elif inic > fim:
        while inic >= fim:
            print(inic, end=' ', flush=True)
            inic -= passo
            sleep(0.5)
        print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Digite o início: ')), int(input('Digite o fim: ')), int(input('Digite o passo: ')))