# crie uma tupla com varias palavras sem acentos .
# mostrar quais as vogais de cada palavra

list = ('carro', 'moto', 'aviao', 'barco', 'navio')
for palavra in list:
    print(f'A palavra {palavra.upper()} possui as seguntes vogais: ', end=' ')
    for letra in palavra:
        if letra.upper() in 'AEIOU':
            print(letra.upper(), end=' ')
    print()