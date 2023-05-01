import shelve

d = shelve.open('/home/pokky/Documents/coding/python/exercicios2/modulos/exercicioss/ex115/cadastros', 'c')

for p in d:
    print(p)