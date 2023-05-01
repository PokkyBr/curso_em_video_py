lista = 'pão', '4', 'remédio', '20', 'lápis', '5.50', 'pastel', '7.50'
for c in range(0, len(lista), 2):
    print(f'{lista[c]} = R${lista[c+1]}')