from time import sleep


def count(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end='...')
            sleep(0.5)
            cont += p
        print('Fim')
        print('-=' * 24)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end='...')
            sleep(0.5)
            cont -= p
        print('Fim')
        print('-=' * 24)


count(1, 10, 1)
count(10, 0, 2)
i = int(input('Inicio: '))
f = int(input('Final: '))
p = int(input('Passo: '))
print('-=' * 24)
count(i, f, p)