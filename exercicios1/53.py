f = input('Digite uma frase: ').replace(' ', '')
g = ''.join(reversed(f))
if f == g:
    print('Palíndromo')
else:
    print('Não palíndromo')