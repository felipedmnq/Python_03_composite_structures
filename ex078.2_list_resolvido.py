# leia 5 valores e coloque-os em uma lista. Mostrar maior e menor valor e suas posiçoes na lista.
# caso o numero se repita, deve mostrar todas as posições que ele se encontra.

lista = []
maior = 0
menor = 0
for cont in range(0, 5):
    lista.append(int(input(f'Gigite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = lista[cont]
    else:
        if lista[cont] > maior:
            maior = lista[cont]
        if lista[cont] < menor:
            menor = lista[cont]
print('=' * 50)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor digitado foi {maior}, nas posições: ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}... ', end='')
print()
print(f'O menor valor digitado foi {menor}, nas posições: ', end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice}... ', end='' )
print()
