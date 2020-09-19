# função notas() que pode receber várias notas de alunos retornando um dicionário com as seguintes informações:
# A) quantidade de notas. B) A maior nota. C) a menor nota. D) A média da turma. E) a Siuação (opcional).
# Adicionar docstrings. ver video 45min

inf = {}
def notes(*notas, sit=False):
    """
        - Pode-se adicionar em notas quantas notas desejar, e fica opcional analisar a situação.
    :param notas: Notas dos alunos - quantas desejar
    :param sit: opcional - situação da média das notas.
    :return:    -   TOTAL de notas.
                -   MAIOR nota.
                -   MENOR nota.
                -   MÉDIA das notas.
                -   SITUAÇÃO (opcional) - ótima/boa/ruim.
    """
    inf['TOTAL'] = len(notas)
    inf['MAIOR'] = max(notas)
    inf['MENOR'] = min(notas)
    inf['MÉDIA'] = sum(notas) / len(notas)
    if sit:
        if inf['MÉDIA'] > 7:
            inf['SITUAÇÃO'] = 'ÓTIMA'
        if inf['MÉDIA'] >= 5:
            inf['SITUAÇÃO'] = 'BOA'
        else:
            inf['SITUAÇÃO'] = 'RUIM'
    return inf


notes(5, 4.4, 9, 7, 2, 5.8, sit=True)
print(inf)
help(notes)