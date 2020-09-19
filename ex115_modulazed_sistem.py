# Crie um sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# o sistema terá duas opçoes: cadastrar uma nova pessoa e listar as pessoas cadastradas.

lst = []


def register1():
    dic = {}
    dic['name'] = input('Nome: ')
    dic['idade'] = input('Idade: ')
    lst.append(dic)

def menu_princ():
    init = 'MENU PRINCIPAL'
    tam = len(init) + 20
    print('\033[1;32m-' * tam)
    print(f'          {init}')
    print('\033[1;32m-\033[m' * tam)
    print('\033[1;33m1 - \033[m', '\033[1;34mVer pessoas cadastradas.\033[m'
          '\n\033[1;33m2 - \033[m', '\033[1;34mCadastrar nova pessoa.\033[m'
          '\n\033[1;33m3 - \033[m', '\033[1;34mSair do sistema.\033[m')
    print('\033[1;32m-\033[m' * tam)


def leiaSTR(msg):
    while True:
        try:
            name = str(input(msg)).strip()
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO!!! Por favor, digite um nome válido!\033[m')
            continue
        else:
            name2 = name.split()
            n_name = ''
            for t in name2:
                n_name += t
            if not n_name.isalpha():
                print(f'\033[1;31mERRO!!! Por favor, digite um nome válido!\033[m')
                return leiaSTR(msg)
            else:
                return msg



name = leiaSTR('Nome: ')
print(name)