def notas(*num, sit=False):
    """
    :param num: Notas
    :param sit: Valor opcional; Mostrar a situação ou não
    :return: dicionário com várias informações sobre a turma
    """
    notass = {}
    notass['total'] = len(num)
    """for pos, n in enumerate(num):
        if pos==0:
            notass['maior'] = n
            notass['menor'] = n
        else:
            if notass['maior'] < n:
                notass['maior'] = n
            if notass['menor'] > n:
                notass['menor'] = n""" #solução do Guanabara mt mais eficaz
    notass['maior'] = max(num)
    notass['menor'] = min(num)
    notass['média'] = sum(num) / len(num) #esse eu pensei sozinho
    if sit:
        if notass['média'] >= 9:
            notass['situação'] = 'ÓTIMA'
        elif notass['média'] >= 7:
            notass['situação'] = 'BOA'
        elif notass['média'] >= 5:
            notass['situação'] = 'RAZOÁVEL'
        elif notass['média'] >= 3:
            notass['situação'] = 'RUIM'
        else:
            notass['situação'] = 'EXTREMAMENTE RUIM'
    return notass

resp = notas(2,2,3,4,6,7,9,7,6,8, sit=True)
print(resp)