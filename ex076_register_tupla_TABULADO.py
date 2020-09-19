# crie uma tupla unica com nomes de produtos e seus preços em sequencia.
# no fianl mostrar listagem com os dados em forma tabular

list = ('Caderno', 20, 'Lápis', 1.5, 'Caneta', 3.25, 'Dicionário', 16.5, 'Calculadora HP', 128, 'Mochila', 98)
print('=' * 50)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('=' * 50)
for c in range(0, len(list), 2):
    print(f'{list[c]:.<40}', end='')
    print(f'R${list[c + 1]:>7.2f}')         # o "7" representa a quantidade de caracteres a esquerda.
print('=' * 50)                             # o ".2f" representa duas casas decimais
