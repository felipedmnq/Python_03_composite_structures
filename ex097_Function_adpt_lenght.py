# função escreva() que receba um texto como parametro e mostre uma mensagem com tamamho adaptavel. OLA MUNDO


def write(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


write('Felipe Demenech vasconcelos')
write('Olé Mundo!!!!')

