# Rescreva a função leiaInt() (ex104) incluindo possibilidade de digitação de um numero de tipo invalido.
# Criar função leiaFloat() com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO!!! Por favor, digite um número INTEIRO válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;34mO usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return num


def leiaFloat(msg):
    while True:
        try:
            num = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO!!! Por favor, digite um número REAL válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;34mO usuário preferiu não digitar um número.\033[m')
            return 0
        else:
            return num



n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O número INTEIRO digitado foi {n1}.\nO número REAL digitado foi {n2}')





