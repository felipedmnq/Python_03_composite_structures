# funçao contador(), receba 3 par metros: inicio, fim e passo e realize a contagem.
#3 contagems: A)  de 1 a 10 de um em um B) 10 a 0 de 2 em 2 C)contagem personalizada. ver condições personalizadas no video
# 45 min no video
from time import sleep


def count(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 26)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if i > f:
        f -= 1
    if i < f:
        f += 1
    for c in range(i, f, p):
        print(c, end='...')
        sleep(0.5)
    print('Fim.')
    print('-=' * 26)


count(0, 10, 1)
count(10, 0, 2)
i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
count(i, f, p)
print(f'Inicio = {i}, final = {f}, passo = {p}.')