# registro: nome; nascimento; CTPS; idede. cadastrar em um dicionário. se CTPS for diferente de 0, também recebera
# ano de contratação e salario. calcular em quantos anos vai se aposentar. (35 anos de contribuição aposenta)
from datetime import date
list = []
register = {}
while True:
    register['Nome'] = str(input('Nome: '))
    register['Ano de nascimento'] = int(input('Ano de nascimento: '))
    register['Idade'] = date.today().year - register['Ano de nascimento']
    register['CTPS'] = int(input('Número da CTPS [0 caso não tenha]: '))
    if register['CTPS'] != 0:
        register['Ano contratação'] = int(input('Ano de contratação: '))
        register['Salario'] = float(input('Salário(R$): '))
        register['Aposentadoria'] = 35 - (date.today().year - register['Ano contratação'])
    list.append(register.copy())
    register.clear()
    while True:
        cont = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
for k, v in list.items():
    print(f'{k}: {v}')
