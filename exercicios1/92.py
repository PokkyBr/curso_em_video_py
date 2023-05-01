from datetime import datetime
date = datetime.today()
year = date.year
pessoa = {}
while True:
    pessoa['nome'] = input('Digite seu nome: ')
    pessoa['idade'] = nascimento = int(input('Ano de nascimento: '))
    pessoa['idade'] = year - pessoa['idade']
    pessoa['ctps'] = int(input('CTPS (0 não tem): '))
    if pessoa['ctps'] == 0:
        break
    pessoa['contratação'] = int(input('Digite o ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - nascimento
    break

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')