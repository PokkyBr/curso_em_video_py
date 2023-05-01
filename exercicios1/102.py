def fatorial(num, show=False):
    """
    -> Calculao fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número.
    """
    f = 1
    for n in range(num, 0, -1):
        f*=n
    if show == True:
        for n in range(num, 0, -1):
            if n > 1:
                print(f'{n} x', end=' ')
            else:
                print(f'{n} = ', end='')
        return f
    return f

print(fatorial(5, True))