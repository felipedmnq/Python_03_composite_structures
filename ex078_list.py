# leia 5 valores e coloque-os em uma lista. Mostrar maior e menor valor e suas posiçoes na lista.
# caso o numero se repita, deve mostrar todas as posições que ele se encontra.

#val = []
#for cont in range(0, 5):
#    val.append(int(input('Digite um valor: ')))
#print(f'Você digitou os valores: {val}')
#print(f'O maior valor digitado foi {max(val)}, na posição {val.index(max(val))}')
#print(f'O menor valor digitado foi {min(val)}, na posição {val.index(min(val))}')

lista = []
for i in range(0, 5):
    lista.append(int(input(f'Digite o valor da posição {i}: ')))
maior = 0
menor = 0
print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi {max(lista)}, na posição: ', end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {min(lista)}, na posição: ', end=' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')



