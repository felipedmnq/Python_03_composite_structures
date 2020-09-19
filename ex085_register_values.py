# digitar 7 valores numeericos EM UMA LISTA UNICA, mante do separados os pares e impares.
# mostrar pares e impares em ordem crescente.
lista = []
for c in range(0, 7):
    lista.append(int(input(f'Digite o {c + 1}º valor: ')))
lista.sort()
print('-=' * 30)
print('Os valores pares digitados foram: ', end=' ')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
print('\nOs valores ímpares digitados foram: ', end=' ')
for c in lista:
    if c % 2 != 0:
        print(c, end=' ')
print()
print('-=' * 30)

