i=0
i2=0
for c in range(1, 501, 2):
    i+=1
    if i % 3 == 0:
        i2 += i
print(i2)