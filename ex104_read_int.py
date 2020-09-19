# crie a função leiaint() que funcionara como o "input", porém fazendo validação para aaceitar apenas valores numericos
# Ex: n = leiaint('Digite um numero: ')


def leiaint():
    while True:
        print('-' * 20)
        num = input('Digite um número: ')
        if not num.isdigit():
            print('\033[1;31mERRO! Apenas números inteiros são aceitos.\033[m')
        else:
            break
    print(f'O número digitado foi: {num}.')


leiaint()


