# usuario digita 5 valores numericos. os valores devem ser cadastrados automaticamente na ordem
# nao pode usar .sort.  mostrar a lista na tela. mostrar na tela a posição que está sendo inserido.
lista = []
for c in range(0, 5):
    num = int(input('Gigite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'Os valores digitados foram {lista}')
