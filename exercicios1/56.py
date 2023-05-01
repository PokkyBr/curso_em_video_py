idd = 0
i=0
j=0
for c in range(0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    sexo = input('Qual seu sexo? masc ou fem: ')
    idd+=idade
    if sexo == 'masc':
        if i <= idade:
            i = idade
            name = nome
    if sexo == 'fem':
        if idade < 20:
            j+=1

print(f'A média de idade do grupo é de {idd/(c+1)}, o nome do homem mais velho é {name} e {j} mulheres têm menos de 20 anos.')