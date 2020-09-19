# usuário pode digitar válios valores, cadastre-os em uma lista. Caso o numero ja exista na lista, nao será adicionado
# exibir todos os valores digitados na ordem do crescente.
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado, não será inserido na lista.')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso.')
    while True:
        n = str(input('Deseja continuar? [S/N]: ')).upper().split()[0]
        if n in 'SN':
            break
    if n in 'N':
        break
lista.sort()
print(lista)
