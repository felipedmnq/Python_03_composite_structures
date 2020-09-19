from random import randint
from time import sleep
lista = list()
temp = list()
tot = 1
print('=#' * 15)
print('{:^30}'.format('SORTEADOR MEGA SENA'))
print('=#' * 15)
qt = int(input('Quantos jogos deseja sortear?: '))
while tot <= qt:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    lista.append(temp[:])
    temp.clear()
    tot += 1
print('{:^30}'.format('SORTEANDO JOGOS...'))
print('=#' * 15)
for i, l in enumerate(lista):
    print(f'{i + 1}º JOGO: {l}')
    sleep(1)
print('=#' * 15)
print('{:^30}'.format('BOA SORTE!'))
print('=#' * 15)
