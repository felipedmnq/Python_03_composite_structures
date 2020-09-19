from random import randint
from time import sleep
from operator import itemgetter
dice = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = []
print('VALORES SORTEADOS: ')
for k, v in dice.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(dice.items(), key=itemgetter(1), reverse=True)   # para colocar o dicionário em ordem (inversa).  # monta uma lista.
print('{:=^34}'.format('RANKING'))
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
print("=" * 34)
