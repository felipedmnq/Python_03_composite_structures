# gerar 5 numeros aleatórios e colocá-los dentro de uma tupla
# mostrar a lista dos numeros, qual o menor e qual o maior

from random import randint
list = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),)
print(f'Os números sorteados foram: ', end='')
for n in list:
     print(f'{n} ', end='')
print(f'\nO maior número foi {sorted(list)[4]}.\nO menor número sorteado foi 'f'{sorted(list)[0]}.')
print('=' * 30)
print(f'Os números sorteados foram {list}, sendo o maior número {max(list)} e o menor número {min(list)}.')
print('FIM DO PROGRAMA')