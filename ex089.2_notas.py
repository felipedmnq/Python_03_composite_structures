lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota do 1º semestre: '))
    nota2 = float(input('Nota do 2º semestre: '))
    media = float((nota1 + nota2) / 2)
    lista.append([nome, [nota1, nota2], media])
    while True:
        resp = str(input('Quer continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"Nº":<5}{"Nome":<10}{"Média":>8}')
print('-=' * 30)
for i, a in enumerate(lista):
    print(f'{i:<5}{a[0]:<10}{a[2]:7.2f}')
while True:
    print('-' * 35)
    resp = int(input('Detalhar notas de qual aluno? [999 interrompe]: '))
    if resp == 999:
        print('Finalizando...')
        break
    if resp <= len(lista):
        print(f'Notas de {lista[resp][0]} são {lista[resp][1]}')
print('VOLTE SEMPRE!')
