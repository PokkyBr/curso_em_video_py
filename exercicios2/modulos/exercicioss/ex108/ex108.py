from ex108 import moeda


n = float(input('Digite o preço: R$'))
print(f'Aumentando 10% de {moeda.moeda(n)}, temos {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é igual a {moeda.moeda(moeda.metade(n))}')
print(f'Reduzindo 13% de {moeda.moeda(n)}, temos {moeda.moeda(moeda.diminuir(n, 13))}')