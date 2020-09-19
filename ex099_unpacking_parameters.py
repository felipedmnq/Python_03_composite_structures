# função maior() que receba varios parametros com valores int. analisar os valores e dizer qual o maior.
# informar quantos valores foram informados e qual o maior. usar função sleep.
from time import sleep


def bigger(* num):
    print('Analisando os valores informados...')
    sleep(1)
    for v in num:
        print(f'{v} - ', end='')
        sleep(0.5)
    print('Fim')
    print(f'Foram informados {len(num)} parâmetros e o maior é: {max(num)}.')
    print('-=' * 24)


bigger(2, 4, 5, 1, 6, 7, 8, 9, 10, 2)
bigger(0, 2)
bigger(5, 6, 1, 9)
#bigger()    - dessa forma da erro quando não é informado nenhum pararametro

