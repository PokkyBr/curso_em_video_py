def leiadinheiro(msg):
    while True:
        """din = input(msg).strip().replace(',', '.')""" #jeito do Guanabara (tem erro ao colocar letras com números)
        """if din.isalpha() or din == '':
            print(f'\33[0;31m"{din}" não é um valor válido.\33[m')
        else:
            return float(din)"""
        din = input(msg).strip()
        if din.count(',') == 1 or din.count(',') == 0:
            if din.find(',') != -1:
                lug = din.find(',')
                din = din.replace(',', '')
                print(din, lug)
            if din.isnumeric():
                if str(lug).isnumeric():
                    din = din[:lug] + '.' + din[lug:]
                    print(din)
                    return float(din)
                return float(din)
            else:
                print(f'\33[0;31m"{din}" não é um valor válido.\33[m')
        else:
                print(f'\33[0;31m"{din}" não é um valor válido.\33[m')