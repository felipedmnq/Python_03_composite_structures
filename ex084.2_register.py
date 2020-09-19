cad = []
pessoas = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(cad) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    cad.append(pessoas[:])
    pessoas.clear()
    while True:
        continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 40)
print(f'Foram cadastradas {len(cad)} pessoas.')
print(f'O maior peso foi de {maior}Kg Peso de ', end='')
for p in cad:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in cad:
    if p[1] == menor:
        print(f'{p[0]}')

