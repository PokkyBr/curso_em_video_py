menor=soma=i=0
cont=''
while True:
    nome = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço do produto: '))
    soma = soma+preço
    if preço > 1000:
        i+=1
    if menor == 0:
        menor = preço
        barato = nome
    if menor >= preço:
        barato = nome
        pbarato = preço
    while cont != 'Y' and cont != 'N':
        cont = input('Quer continuar? (Y/N)').upper()
    if cont == 'N':
        break
    cont=''

print(f'O valor total gasto na compra foi de R${soma:.2f}\n{i} produtos custam mais de R$1000\nO produto mais barato se chama {barato} e custa R${pbarato:.2f}.')
