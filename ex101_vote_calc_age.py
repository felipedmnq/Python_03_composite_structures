# programa com função vote() recebe parametro ano de nascimento e retorna valor literal, se a pessoa tem
# voto NEGADO, OPCIONAL, OBRIGATÓRIO. (> 65 é opcional).
from datetime import date


def vote(nasc = 0):
    """
    :param nasc: receives the voter's birth year.
    :return: if the voter is denied the vote, if it is optional or if the vote is mandatory.
    """
    age = date.today().year - nasc
    if age <16:
        print('-' * 48)
        print(f'\033[1;31mO eleitor tem {age} anos e o voto foi NEGADO.\033[m')
    if age >= 16 and age < 18 or age >= 65:
        print('-' * 48)
        print(f'\033[1;33mO eleitor tem {age} anos e o voto é OPCIONAL.\033[m')
    if age >= 18 and age < 65:
        print('-' * 48)
        print(f'\033[1;34mO eleitor tem {age} anos e o voto é OBRIGATÓRIO.\033[m')


nasc = int(input('Ano de nascimento do eleitor: '))
vote(nasc)
help(vote)