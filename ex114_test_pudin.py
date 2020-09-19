# codigo que teste se o site Pudim está acessivel pelo computador do usuario


import urllib
import urllib.request


def siteOK():
    try:
        urllib.request.urlopen('http://pudim.com.br/')
    except Exception as erro:
        print('\033[1;31mO site não está acessivel no momento\033[m')
    else:
        print('\033[1;34mO site está com acesso normal\033[m')


siteOK()

