# leia varios numeros e coloque na lista
# criar duas listas extras - pares e impares
# mostrar as 3 listas.
# dica - primeiro ler os valores, depois separar em outras duas listas.

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    while True:
        c = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
par = []
impar = []
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print(f'Números digitados: {lista}.\nNúmeros pares digitados: {par}.\nNúmeros ímpares digitados: {impar}')
