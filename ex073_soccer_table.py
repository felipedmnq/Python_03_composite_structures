# crie uma tupla com o 20 primeiros colocados do brasileirao na ordem de colocação
# mostre - A) Apenas os 5 primeiros. B) os 4 ultimos. C) em ordem alfabética. D) posição da CHAPE.

br = ('Vasco da Gama', 'Internacional', 'Atlético MG', 'Bahia', 'Santos', 'Athletico PR', 'Gremio', 'Botafogo',
      'Palmeiras', 'Bragantino SP', 'Corinthians', 'Atlético GO', 'São Paulo', 'Fluminense', 'Fortaleza', 'Sport',
      'Flamengo', 'Goiás', 'Ceará SC', 'Cotibiba')
print('=' * 50)
print('{:^50}'.format('5 PRIMEIROS COLOCADOS'))
print(br[:5])
print('=' * 50)
print('{:^50}'.format('4 ÚLTIMOS COLOCADOS'))
print(br[-4:])
print('=' * 50)
print('{:^50}'.format('EM ORDEM ALFABETICA'))
print(sorted(br))
print('=' * 50)
print('{:^50}'.format('POSIÇÃO DO SÃO PAULO FC'))
print('O São Paulo ocupa atualmente a {}º posição no Brasileirão 2020.'.format(br.index('São Paulo') + 1))
print(f'O São Paulo ocupa atualmente a {br.index("São Paulo") + 1}º posição no brasileirão 2020.')
print('=' * 50)
for times in br:
      print(times)
