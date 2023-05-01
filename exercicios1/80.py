valores = []
for c in range(0,5):
    a = int(input('Digite um valor: '))
    if c == 0 or a > valores[-1]:
        valores.append(a)
    else:
        pos = 0
        while pos < len(valores):
            if a < valores[pos]:
                valores.insert(pos, a)
                break
            pos+=1


print(valores)