expr = str(input('Digite a expressão: '))
abre = []
for simb in expr:
    if simb == '(':
        abre.append('(')
    elif simb == ')':
        if len(abre) > 0:
            abre.pop()
        else:
            abre.append(')')
            break
if len(abre) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão é inválida!')