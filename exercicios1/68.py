import random
i=0
b=''
while True:
    v = int(input('Digite um valor: '))
    pi = input('Par ou ímpar? [P/I]').upper()
    c = random.randint(1,6)
    if (v+c) % 2 == 0:
        a = 'P'
        print(f'{b:=>30}\nVocê jogou {v} e o computador {c}. Total de {v+c} deu PAR')
    else:
        a = 'I'
        print(f'{b:=>30}\nVocê jogou {v} e o computador {c}. Total de {v+c} deu ÍMPAR')
    if pi == a:
        print(f'{b:=>30}\nVocê venceu!\nVamos jogar novamente...')
        i+=1
    else:
        break
print(f'{b:=>30}\nGAME OVER! Você venceu {i} vezes.')