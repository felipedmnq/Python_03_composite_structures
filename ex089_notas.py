# leia nome e DUAS notas de vários alunos eguarde tudo em uma lista composta.
# mostrar boletim com a média e permitir que o usuario veja a nota individual de cada aluno.
# são tres niveis de lista, uma dentro da outra. tudo em uma unica lista.
lista = []
temp = []
notas = 0
while True:
    aluno = str(input('Nome: '))
    temp.append(aluno)
    nota1 = float(input('Nota 1º Semestre: '))
    temp.append(nota1)
    nota2 = float(input('Nota 2º Semestre: '))
    temp.append(nota2)
    media = (nota1 + nota2) / 2
    temp.append(media)
    lista.append(temp[:])
    temp.clear()
    while True:
        resp = str(input('Deseja continuar cadastrando?: [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('=' * 40)
print('{:<}   {:<30}{}'.format('Nº', 'ALUNO', 'MÉDIA'))
for c in range(0, len(lista)):
    print(f'{(c + 1):<5}{lista[c][0]:.<30}{lista[c][3]:.2f}')
print('=' * 40)
while True:
    while True:
        resp = str(input('Detalhamento de nota? [S/N]: ')).upper().strip()[0]
        if resp == 'N':
            break
        notas = int(input('Deseja ver as notas de qual aluno?: '))
        if notas > len(lista) or notas < 1:
            print('Dado incorreto. Tente novamente.')
        else:
            print(f'As notas de {lista[notas - 1][0]} foram: {lista[notas - 1][1:3]}')
    if resp == 'N':
        break