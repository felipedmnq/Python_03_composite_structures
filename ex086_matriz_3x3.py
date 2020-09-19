# crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
# mostrar a matriz com formatação correta.
matriz = [[], [], []]
for c in range(0, 3):
    for i in range(0, 3):
        matriz[c].append(int(input(f'Digite um valor para [{c},{i}]: ')))
print('-=' * 20)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[{matriz[c][i]:^5}]', end='')
    print()
print('-=' * 20)
