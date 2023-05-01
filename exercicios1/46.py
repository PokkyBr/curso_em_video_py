import time
d = 0
i=10
for c in range(d, d+10):
    print(f'{i} segundos')
    i -= 1
    time.sleep(1)
print('BUM!')