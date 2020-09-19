# leia a média de um aluno e sua situação. > 7 - aprovado. < 7 reprovado.
#nome: ccccc. média: xxx; situação: ap/rp

students = {}
students['name'] = str(input('Nome do aluno: '))
students['avg'] = float(input(f'Média do aluno {students["name"]}: '))
print('-=' * 20)
print(f'O nome do aluno é {students["name"]}')
print(f'A média do aluno é: {students["avg"]}')
if students['avg'] < 5:
    students['situation'] = 'REPROVADO'
    print('Aluno REPROVADO')
elif 5 <= students['avg'] < 7:
    students['situation'] = 'EM RECUPERAÇÃO'
    print('Aluno EM RECUPERAÇÃO.')
else:
    students['situation'] = 'APROVADO'
    print('Aluno APROVADO.')
print('-=' * 20)
for k, v in students.items():
    print(f'{k} é igual a {v}')
print(students)
