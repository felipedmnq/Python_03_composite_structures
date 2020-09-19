from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de trabalho [0 = não tem CTPS]: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$ '))
    dados['aposentadoria'] = (35 - (date.today().year - dados['contratacao']) + dados['idade'])
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k}: {v}')