# usuário deve digitar uma expressão matemática que use parenteses.
# ver o video para saber o resultado.

lista = []
check = 0
while True:
    exp = str(input('Digite uma expressão matemática para saber se ela é válida: '))
    for c in exp:
        if c == '(' or c == ')':
            lista.append(c)
    for i in lista:
        if i == '(':
            check += 1
        elif i == ')':
            check -= 1
        elif check < 0:
            break
    if check == 0:
        print('Expressão válida.')
    else:
        print('Expressão inválida.')
    while True:
        c = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        if c in 'SN':
            break
    if c == 'N':
        break
