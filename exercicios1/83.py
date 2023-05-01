'''i=0
exp = input('Digite a expressão: ')
for letras in exp:
    if letras in '()':
        i+=1

if i % 2 ==0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')'''
#dá pra arrumar mas to com preguiça
#---------------------------------------------------------#
exp = input('Digite a expressão: ')
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
    
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')