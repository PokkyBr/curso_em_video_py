numeros = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
a = -1
while a < 0 or a > 20:
    a = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {numeros[a]}.')