cores = {
    'padrao': '\33[m',
    'azul': '\33[1;34m',
    'amarelo': '\33[1;33m',
    'vermelho': '\33[1;31m'
}

def linha():
    print('~'*40)

def cor(msg, cor='amarelo'):
    return f'{cores[cor]}{msg}{cores["padrao"]}'

def menu():
    linha()
    print('MENU PRINCIPAL'.center(40))
    linha()
    print(f'{cor("1 - ", "amarelo")}{cor("Ver pessoas cadastradas", "azul")}')
    print(f'{cor("2 - ", "amarelo")}{cor("Cadastrar nova Pessoa", "azul")}')
    print(f'{cor("3 - ", "amarelo")}{cor("Sair do Sistema", "azul")}')
    linha()

def leiaint(msg):
    global n
    while True:
        n = input(msg)
        if n.isnumeric():
            break
        print('\33[0;31mERRO! Digite um número inteiro válido.\33[m')
    return n