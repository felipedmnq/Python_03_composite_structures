# fazer função area() que receba as dimensoes de um terreno retangular e mostre a area do terreno.


def area(l, c):
    areaTerr = l * c
    print(f'O terreno com dimensões {a}m x {b}m possui área total de {areaTerr}m².')


c = float(input('Qual o comprimento do terreno em metros?: '))
l = float(input('Qual a largura do terreno em metros?: '))
area(l, c)
