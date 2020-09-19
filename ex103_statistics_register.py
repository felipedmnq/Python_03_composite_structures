# função ficha, recebe dois parametros: nome de um jogador e quantos gols marcou
# devera retornar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def player(name='<Unknown>', gols=0):
    """
    - Plyaers scores.
    :param name: Player's name
    :param gols: number of goals of the player in the championship.
    :return: Players name / gols
    """
    print(f'O jogador {name} fez {gols} gol(s) no campeonato.')


name = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name.strip() == '':
    player(gols = gols)
else:
    player(name, gols)
