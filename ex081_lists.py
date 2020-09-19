#usuario digita vários numeros. mostrar: A) quantos numeros foram digitados. B) lista em odem inversa
# C) se o valor 5 foi digitado e se esta na lista.

lista = []
cont = 0
cont5 = 0
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    #cont += 1
    if num == 5:
        cont5 += 1
    while True:
        c = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
#print(f'Foram digitados {cont} valores.')
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Lista invertida: {lista}')
#if 5 in lista:
if cont5 != 0:
    print(f'O número 5 foi digitado {cont5} vezes.')
else:
    print('O número 5 não foi digitado')
