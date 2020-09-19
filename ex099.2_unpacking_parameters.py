from time import sleep


def bigger(* num):
    cont = bigger = 0
    print('\nAnalisando os valores informaos...')
    for v in num:
        print(f'{v} - ', end='')
        sleep(0.4)
        if cont == 0:
            bigger = v
        else:
            if v > bigger:
                bigger = v
        cont += 1
    print('Fim')
    print(f'Foram analisados {cont} valores e o maior foi {bigger}')
    print('-=' * 25)


bigger(2, 9, 4, 5, 7, 1)
bigger()
bigger(1, 8)