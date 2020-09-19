#leia 4 valores pelo teclado e guarde-os em uma tupla
# A) quantas vezes apareceu o "9". B) Posição do 1º "3". C) quais os numeros pares.
# mostrar caso o 3 nao seja digitado

list = (int(input('Digite um número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite o último número: ')))
print(f'Você digitou os números: {list}')
print(f'O número 9 apareceu {list.count(9)} vezes.')
if 3 in list:
    print(f'O número 3 apareceu na {list.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado.')
print('Os valores pares digitados foram:', end= ' ')
for n in list:                                          #método mais prático para procurar os pares.
    if n % 2 == 0:
        print(n, end=' ')
if list[0] % 2 == 0 or list[1] % 2 == 0 or list[2] % 2 == 0 or list[3] % 2 == 0:
    print('\nOs valores pares digitados foram:', end= ' ')
    if list[0] % 2 == 0:
        print(list[0], end='. ')
    if list[1] % 2 == 0:
        print(list[1], end='. ')
    if list[2] % 2 == 0:
        print(list[2], end='. ')
    if list[3] % 2 == 0:
        print(list[3], end='. ')
else:
    print('Não foram digitados números pares.')