# aprimorar o ex093. com varios jogadores. incluir sistema de viasualização de detalhes do aproveitamento de cada jogador.

player = dict()
gols = list()
lista = list()
cod = 0
while True:
    player['name'] = str(input('Nome do jogador: '))
    matchs = int(input(f'Quantas partidas {player["name"]} jogou?: '))
    for c in range(0, matchs):
        gols.append(int(input(f'Quantos gols {player["name"]} fez na {c + 1}ª partida?: ')))
    player['gols'] = gols[:]
    player['total'] = sum(gols)
    lista.append(player.copy())
    gols.clear()
    player.clear()
    while True:
        cont = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
print('-=' * 25)
print(lista)
print('-=' * 25)
print('{:^5}{:<20}{:<20}{:<5}'.format('Cod', 'Nome', 'Gols', 'Total'))
print('-=' * 25)
for k, v in enumerate(lista):
    print(f'{(k + 1):^5}', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-=' * 25)
while True:
    stat = int(input('Digite o código do jogador para visualizar as estatísticas [999 para sair]: '))
    stat -= 1
    if stat == 999:
        break
    if stat < 0 or stat > len(lista):
        print('Jogador inexistente! Tente novamente!')
    else:
        print(f' -- ESTATÍSTICAS DO JOGADOR {lista[stat]["name"].upper()} --')
        print('-=' * 19)
        for i, g in enumerate(lista[stat]["gols"]):
            print(f'      - No {i + 1}º jogo fez {g} gols.')
    print('-=' * 19)





