time = []
jogador = {}
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
        if resp in 'SN':
            break
        print('RESPOSNTA INVÁLIDA!')
    if resp == 'N':
        break
print('-=' * 40)
print('Cod ', end='')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:^3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Digite o código do jogador para visualizar as estatísticas [999 para parar]: '))
    if busca == 999:
        break
    if busca < 0 or busca > len(time):
        print('Erro, código inexistente!')
    else:
        print(f' -- ESTATÍSTICAS DO JOGADOR {time[busca]["nome"].upper()} -- ')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    - No jogo {i + 1} fez {g} gols.')
    print('-=' * 40)
print('VOLTE SEMPRE!')
