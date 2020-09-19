list = ('Caderno', 20,
        'Lápis', 1.5,
        'Caneta', 3.25,
        'Dicionário', 16.5,
        'Calculadora HP', 128,
        'Mochila', 98)
print('-' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-' * 40)
for iten in range(0, len(list)):
    if iten % 2 == 0:
        print(f'{list[iten]:.<30}', end='')
    else:
        print(f'R${list[iten]:>7.2f}.')
print('-' * 40)
