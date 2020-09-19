def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isdigit():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO! Apenas números são aceitos.\033[m')
        if ok:
            break
    return valor


n = leiaint('Digite um número: ')
print(f'Você digitou o número: {n}.')