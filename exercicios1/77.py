palavras = 'eu', 'pego', 'nao', 'pego', 'de', 'vez', 'em', 'quando', 'fico', 'admirando'
'''for p in palavras:
    print(f'As vogais da palavra "{p}" são: ', end='')
    if 'a' in p:
        print('a', end=', ')
    if 'e' in p:
        print('e', end=', ')
    if 'i' in p:
        print('i', end=', ')
    if 'o' in p:
        print('o', end=', ')
    if 'u' in p:
        print('u', end=', ')
    print('\n')'''

for p in palavras:
    print(f'\nAs vogais da palavra "{p}" são: ', end='')
    for letras in p:
        if letras in 'aeiou':
            print(letras, end=' ')