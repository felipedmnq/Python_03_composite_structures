# crie uma tupla totalmente preenchida com contagem por extenso de zero até 20.
# programa deve ler um número pelo teclado e mostrá-lo por extenso.

ext = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = 0
while True:
    n = int(input('\033[1;32mDigite um numero entre 0 e 20 para vê-lo por extenso: '))
    while n < 0 or n > 20:
        n = int(input('Digite um numero entre 0 e 20 para vê-lo por extenso: '))
    print('\033[1;33m-=' * 15)
    print(f'O número solicitado foi: {ext[n]}')
    print('\033[1;33m-=' * 15, '\033[m')
    cont = str(input('\033[1;34mDeseja continuar? [S/N]: \033[m')).upper().split()[0]
    while cont not in 'SN':
        cont = str(input('\033[1;34mDeseja continuar? [S/N]: \033[m')).upper().split()[0]
    if cont == 'N':
        break
print('\033[1;31m-=' * 15)
print('{:^30}'.format('FIM DO PROGRAMA.'))
print('\033[1;31m-=' * 15)
