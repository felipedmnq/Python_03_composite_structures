# criar função fatorial, receba dois parametros 1º numero a calcular e o 2º chamado SHOW (valor lógico opcional falso por padrao.)
# indicando se sera mostrado na tela o processo de calculo do fatorial. VIDE VIDEO MIN: 42
# show = True mostra o calculo, Show = False mostra só o resultado.
# colocar DOCSTRINGS


def factorioal(n, show=False):
    """
    --- Factorial calculator.
    :param n: Factorial number to be calculated.
    :param show: (optional) Show or not the calculation.
    :return: Factorial value of "n".
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

print(factorioal(5, True))
help(factorioal)

