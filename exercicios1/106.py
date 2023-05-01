c = ('\33[m', #0 sem cor
     '\33[0;30;41m', #1 vermelho
     '\33[0;30;42m', #verde
     '\33[0;30;43m', #amarelo
     '\33[0;30;44m', #azul
     '\33[0;30;45m', #roxo
     '\33[7;30m' #branco
     )


"""def linha(msg):
    print('\x1b[1;31;47m' + '~'*(len(msg)+2) + '\x1b[0m')
    print('\x1b[1;31;47m' + f' {msg} ' + '\x1b[0m')
    print('\x1b[1;31;47m' + '~'*(len(msg)+2) + '\x1b[0m')

linha('SISTEMA DE AJUDA PyHELP')

while True:
    comando = input('Digite o comando > ')
    linha(f'Acessando o manual do comando "{comando}"')
    if comando == 'FIM' or comando == 'fim':
        break
    print('\x1b[6;30;42m' + help(comando) + '\x1b[0m')
    print()""" #eu estava fazendo certo mas achei que estava errado porque não queria sair do help, mas isso é do python

def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)gg
    print(c[0], end='')


def título(msg, cor=0):
    tam = len(msg) +4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~'*tam)
    print(c[0])

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)