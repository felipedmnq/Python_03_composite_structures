list = ('carro', 'moto', 'aviao', 'barco', 'navio')
for palavra in list:
    print(f'\nNa paravra {palavra.upper()} temos: ', end= '')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end= ' ')
