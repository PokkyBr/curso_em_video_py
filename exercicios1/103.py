"""def ficha(nome='<desconhecido>', gols=0):
    return nome, gols



#meu código:
if nome == '' and gols != '':
    a = ficha(gols=gols)
elif nome != '' and gols == '':
    a = ficha(nome=nome)
elif nome == '' and gols == '':
    a = ficha()
else:
    a = ficha(nome, gols)

print(f'o jogador {a[0]} fez {a[1]} gol(s) no campeonato.')"""

nome = input('Nome do Jogador: ')
gols = input('Número de gols: ')

#código do Guanabara:
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)