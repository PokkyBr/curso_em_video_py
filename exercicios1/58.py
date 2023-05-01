import random
i=c=0
choice = random.randint(1, 10)
while c != choice:
    c = int(input('Digite um número: '))
    print('Você errou, tente novamente.')
    i+=1
print(f'Você acertou! Foram necessárias {i} tentativas até acertar e o número era {choice}.')