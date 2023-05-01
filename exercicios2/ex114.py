import requests

try:
    x = requests.get('http://pudim.com.br/')
except:
    print('\33[1;31mNão pude acessar o site do pudim :(\33[m')
else:
    print('\33[1;32mConsegui acessar o site do pudim :)\33[m')