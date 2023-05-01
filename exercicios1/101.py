def voto(nasc):
    from datetime import date
    year = date.today().year
    idd = year - nasc
    if idd >= 18 and idd < 65:
        return f'Com {idd} anos: VOTO OBRIGATÓRIO.'
    elif idd >= 16 and idd < 18 or idd >= 65:
        return f'Com {idd} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idd} anos: NÃO VOTA.'


nasc = int(input('Digite sua data de nascimento: '))
print((voto(nasc)))