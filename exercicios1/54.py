from datetime import date
date = date.today()
a = int(date.strftime('%Y'))

i=0
for c in range(1, 8):
    bday = int(input('Informe sua data de nascimento: '))
    if a-bday >= 18:
        i+=1

print(c)
print(f'{i} pessoas já atingiram a maioridade e {c-i} pessoas ainda não atingiram a maioridade.')