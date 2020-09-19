# 4 jogadores jogam um dado. gurdar em um dicionário. colocar em ordem de vencedor

from random import randint
from time import sleep

list = []
dice = {}
for c in range(0, 4):
    dice[f'player {c + 1}'] = randint(1, 6)
    list.append(dice.copy())
    print(f'O jogador {c + 1} tirou {dice[f"player {c + 1}"]}')
    sleep(1)
    dice.clear()
print('{:=^30}'.format('RANKING DOS JOGADORES'))
print(list)

