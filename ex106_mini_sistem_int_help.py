# faça um mini sistema que utilize o interactive help do python. O usuario digita o comando e o manual vai aparecer.
# quando digitar "Fim" o programa encerra. USE CORES. video 45:30min.


def title(msg, color=0):
    tam = len(msg) + 4
    print('\033[1;34m-\033[m' * tam)
    print(f'\033[1;33m  {msg}\033[m')
    print('\033[1;34m-\033[m' * tam)

def helping():
    """
        - Helping function - Uses the Python Interactive Help. The user just have to insert the name of the function or
        library and the function shows the docstrings.
    :return: DocStrings of the function or library called.
    """
    title('SISTEMA DE AJUDA PyHELP')
    msg = input('\033[1;32mFunção ou bilioteca: \033[m')
    return help(msg)

while True:
    helping()
    while True:
        print('\033[1;31m-\033[m' * 44)
        cont = input('\033[1;31mDo you want help with anything else? [Y/N]: \033[m').upper().strip()[0]
        if cont in 'YN':
            break
    if cont in 'N':
        break
print('\033[1;34mVIELEN DANK!\033[m')
