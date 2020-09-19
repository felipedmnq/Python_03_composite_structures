# crie jogos de 6 numeros. perguntar quantos jogos vai criar. cadastrar tudo em uma lista. tudo em ordem
from random import randint
from time import sleep
lista = []
temp = []
print('-=' * 16)
print('{:^32}'.format('SORTEADOR MEGA-SENA'))
print('-=' * 16)
qt = int(input('Quantos jogos deseja fazer?: '))
while True:
    while len(temp) != 6:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
    temp.sort()
    lista.append(temp[:])
    temp.clear()
    if len(lista) == qt:
        break
print('Os jogos sorteados foram:')
print('-=' * 16)
sleep(1)
for c in range(0, len(lista)):
    print(f'{c + 1}º Jogo : ', lista[c])
    sleep(1)
print('-=' * 16)
