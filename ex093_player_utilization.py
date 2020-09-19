# nome do jogaros; quantas partdas jogou; gols por partida(dentro de lista). guardar tudo em dicionário com total de gols.
# ver app operando no videos, sao tres niveis.

data = {}
gols = []
total = 0
data['Jogador'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {data["Jogador"]} jogou?: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}?: ')))
    total += c
data['gols'] = gols
data['total'] = total
print('-=' * 40)
print(data)
print('-=' * 40)
for k, v in data.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 40)
print(f'O jogador {data["Jogador"]} jogou {partidas} partidas.')
for c in range(0, len(gols)):
    print(f'   - Na partida {c + 1}, fez {gols[c]} gols.')
print(f'Total de gols de {data["Jogador"]} = {total}')
print('-=' * 40)
