# leia nome, sexo e idade de varias pessoas. cada pessoa = um dicionario. todos os dicionarios em uma lista. mostrar:
# A) quantas pessoas cadastradas. B) media de idade do grupo. C) lista com mulheres. D) lista com pessoas com idade acima da media.
from datetime import date
lista = []
woman = []
bigage = []
dic = {}
dicw = {}
tot = 0
totage = 0
while True:
    dic['name'] = str(input('Nome: '))
    birth = int(input('Ano de nascimento: '))
    dic['age'] = date.today().year - birth
    totage += dic['age']
    while True:
        dic['sex'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if dic['sex'] in 'MF':
            break
    tot +=1
    lista.append(dic.copy())
    dic.clear()
    while True:
        cont = str(input('Deseja continuar cadastrando? [S/N]: ')).upper().strip()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
ageavg = totage / len(lista)
print('-=' * 30)
print(f'A) Ao todo foram cadastradas {tot} pessoas.'
      f'\nB) A média de idade foi de {ageavg:.2f} anos.'
      f'\nC) As mulheres cadastradas foram: ', end='')
for p in lista:
    if p['sex'] in 'F':
        print(f' {p["name"]} ', end='')
print(f'D) Pessoas com idade acima da média: ')
for i in lista:
    if i['age'] >= ageavg:
        print(f'   - {i["name"]}.')
print('-=' * 30)



