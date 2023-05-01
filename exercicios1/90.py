aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

print(f'Média igual a {aluno["media"]:.1f}')
if aluno['media'] >= 5.0:
    print('Situação: Aprovado')
else:
    print('Situação: Reprovado')