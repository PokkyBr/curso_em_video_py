from funcoes import linha
import shelve

temp = []
pessoa = []

def cadastro():
    global temp
    linha()
    print('NOVO CADASTRO'.center(40))
    linha()
    pessoa.append(input('Nome: '))
    while True:
        idd = input('Idade: ')
        if int(idd):
            int(idd)
            pessoa.append(idd)
            break
        else:
            print('Digite uma idade válida.')
    cadas = shelve.open('/home/pokky/Documents/coding/python/exercicios2/modulos/exercicioss/ex115/cadastros', 'c')
    try:
        temp = cadas['cadastro']
    except KeyError:
        cadas['cadastro'] = pessoa[:]
    temp.append(pessoa.copy())
    cadas['cadastro'] = temp
    print(f'Novo registro de {pessoa[0]} adicionado.')
    pessoa.clear()
