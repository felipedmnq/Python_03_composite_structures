galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! "M" ou "F".')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'NS':
            break
        print('ERRO! "S" ou "N".')
    pessoa.clear()
    if resp == 'N':
        break
media = soma / len(galera)
print('-=' * 30)
print(f'A) Foram cadastradas {len(galera)} pessoas.\n'
      f'B) A média de idade é {media:5.2f}.\n'
      f'C) A mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]},', end='')
print()
print('D) Lista de pessoas com idade acima da média: ')
for i in galera:
    if i['idade'] >= media:
        print(f'  - {i["nome"]}, com {i["idade"]} anos.')
print('-=' * 30)
for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'   - {k} = {v}; ', end='')
        print()
print('-=' * 30)
print('<<<  ENCERRADO  >>>')
