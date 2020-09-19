# aprimore o desafio anterior.
# mostrar - A0 soma de todos os pares. B) soma da 3ª coluna. C) maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
SumPair = Sum3Col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if c == 2:
             Sum3Col += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            SumPair += matriz[l][c]
print('=' * 50)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
    print()
print('=' * 50)
print(f'A soma dos valores da 3ª coluna é: {Sum3Col}.'
      f'\nA soma dos valores pares é: {SumPair}.'
      f'\nO maior valor da 2ª linha é: {max(matriz[1])}.')
print('=' * 50)
