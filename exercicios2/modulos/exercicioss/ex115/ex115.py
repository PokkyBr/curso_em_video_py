import shelve
import funcoes
import pessoas
from time import sleep

while True:
    funcoes.menu()
    opc = 0
    while True:
        try:
            opc = int(input(f'{funcoes.cor("Sua Opção: ")}'))
        except:
            print(funcoes.cor('Digite um número válido', 'vermelho'))
            continue
        if opc == 1 or opc == 2 or opc == 3:
            break
        else:
            print(funcoes.cor('Digite uma opção válida!', 'vermelho'))
            continue
    if opc == 1:
        cadas = shelve.open('/home/pokky/Documents/coding/python/exercicios2/modulos/exercicioss/ex115/cadastros', 'c')
        funcoes.linha()
        print('PESSOAS CADASTRADAS'.center(40))
        funcoes.linha()
        for p in cadas['cadastro']:
            dist = 39 - len(p[0])
            print(f'{p[0]}', f'{p[1]} anos'.rjust(dist))
        cadas.close()
        sleep(1)
    if opc == 2:
        pessoas.cadastro()
        sleep(1)
    if opc == 3:
        break
