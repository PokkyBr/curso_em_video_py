n='a'
while n != 'M' and n != 'F':
    n = input('Digite o seu sexo (M/F): ').upper()
    if n != 'M' and n != 'F':
        print('Digite M ou F.')
print('FIM')