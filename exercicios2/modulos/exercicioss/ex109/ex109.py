import moeda


n = float(input('Digite o preço: R$'))
print(f'Aumentando 10% de {moeda.moeda(n)}, temos {moeda.aumentar(n, 10, form=True)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'A metade de {moeda.moeda(n)} é igual a {moeda.metade(n, form=True)}')
print(f'Reduzindo 13% de {moeda.moeda(n)}, temos {moeda.diminuir(n, 13, form=True)}')