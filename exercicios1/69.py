i=h=m=0
sexo=cont=''
while True:
    idade = int(input('Digite sua idade: '))
    while sexo != 'F' and sexo != 'M':
        sexo = input('Digite seu sexo: (F/M) ').upper()
    if idade >= 18:
        i+=1
    if sexo == 'M':
        h+=1
    if sexo == 'F':
        if idade < 20:
            m+=1
    while cont != 'Y' and cont != 'N':
        cont = input('Quer continuar? (Y/N)').upper()
    if cont == 'N':
        break
    cont=sexo=''

print(f'{i} pessoas tem mais de 18 anos, {h} homens foram cadastrados e {m} mulheres tinham menos de 20 anos.')
