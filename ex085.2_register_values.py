lista = [[], []]
valor = 0
for c in range(0, 7):
    valor = (int(input(f'Digite o {c + 1} valor: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {lista[0]}.'
      f'\nOs valores ímpares digitados foram: {lista[1]}.')
