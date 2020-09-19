# leia varios numeros e coloque na lista
# criar duas listas extras - pares e impares
# mostrar as 3 listas.
# dica - primeiro ler os valores, depois separar em outras duas listas.

lista = []
par = []
impar = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    while True:
        c = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
print(f'Os números digitados foram: {lista}.\nOs números pares foram: {par}.\nOs números ímpares foram: {impar}')