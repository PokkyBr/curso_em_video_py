lista = []
dados = []
while True:
    cont=' '
    dados.append(input('Digite o nome do aluno: ').lower())
    dados.append(int(input('Digite a primeira nota do aluno: ')))
    dados.append(int(input('Digite a segunda nota do aluno: ')))
    lista.append(dados[:])
    dados.clear()
    cont = input('Deseja continuar? (Y/N)').upper()
    if cont in 'N':
        break

for alunos in range(0, len(lista)):
    média = (lista[alunos][1] + lista[alunos][2]) / 2
    print(f'A média do {lista[alunos][0]} foi de {média}')

while True:
    cont=' '
    cont = input('Deseja ver a nota de algum aluno?\n Se sim, digite o nome do aluno, caso não, digite N: ').lower()
    if cont == 'n':
        break
    for pos, aluno in enumerate(lista):
        if cont == aluno[0]:
            print(f'Primeira nota: {aluno[1]}\nSegunda nota: {aluno[2]}')
            break
        elif pos == len(lista)-1:
            print('Nome não encontrado!')
            break
print('-='*30)
print(f'{"PROGRAMA FINALIZADO!":^60}')