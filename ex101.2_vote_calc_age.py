def vote(birth):
    from datetime import date
    age = date.today().year - birth
    if age < 16:
        return f'O eleitor tem {age} anos e teve o voto NEGADO.'
    elif 16 <= age < 18 or age > 65:
        return f'O eleitor tem {age} anos e o voto é OPCIONAL.'
    else:
        return f'O eleitor tem {age} anos e voto é OBRIGATÓRIO.'


birth = int(input('Ano de nascimento: '))
print(vote(birth))