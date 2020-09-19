# leia nome e peso de varias pessoas.
# mostre: A)Quantas pessoas cadastradas. B) Lista dos mais pesados. C) lista dos mais leves.
cad = []
pessoas = []
pes = []
normais = []
lev = []
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    cad.append(pessoas[:])
    if pessoas[1] >= 100:
        pes.append(pessoas[:])
    elif pessoas[1] < 70:
        lev.append(pessoas[:])
    else:
        normais.append(pessoas[:])
    pessoas.clear()
    while True:
        continuar = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if continuar in 'SN':
            break
    if continuar == 'N':
        break
print('-=' * 40)
print(f'Foram cadastradas {len(cad)} pessoas.'
      f'\nOs cadastrados com peso superior a 100kg são: {pes}.'
      f'\nOs cadastrados com peso inferior a 70kg são: {lev}.'
      f'\nOs cadastrados com peso "normal" (entre 70 e 100 kg) são: {normais}')

