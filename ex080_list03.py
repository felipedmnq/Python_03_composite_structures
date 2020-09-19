# usuario digita 5 valores numericos. os valores devem ser cadastrados automaticamente na ordem
# nao pode usar .sort.  mostrar a lista na tela. mostrar na tela a posição que está sendo inserido.
lista = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print(f'O número {num} foi inserido na última posição.')
    else:
        for i in range(0, 5):
            if num <= lista[i]:
                lista.insert(i, num)
                print(f'O número foi adicionado na posição {i}.')
                break
print(lista)
