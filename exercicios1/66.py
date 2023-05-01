i=s=0
while True:
   n = int(input('Digite um número: (999 para parar) ')) 
   if n == 999:
      break
   i+=1
   s = s+n

print(f'Foram digitados {i} números, a soma deles é igual a {s}.')