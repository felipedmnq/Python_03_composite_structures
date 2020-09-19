# faça uma lista chamada numeros, duas funçoes sorteio() e somaPar() . A) sortear 5 numeros B) soma os numeros pares de A
from random import randint
from time import sleep
numbers = []


def sort(lst):
    print('Sorteando 5 valores...', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print(' - Fim')



def sumPair(lst):
    sump = 0
    for v in lst:
        if v % 2 == 0:
            sump += v
    print(f'A soma dos números pares sorteados é: {sump}')


print('-=' * 20)
sort(numbers)
sumPair(numbers)
print('-=' * 20)

