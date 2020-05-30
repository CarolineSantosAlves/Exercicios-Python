from datetime import date
ano = int(input('Informe seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    tempo = 18 - idade
    print('Você deve se alistar em \033[1;34m{} anos'. format(tempo))
    alistar = date.today().year + tempo
    print('Seu alistamento será em {}'.format(alistar))
elif idade == 18:
    print('\033[1;32m É hora de se alistar')
else:
    tempo = idade - 18
    print('\033[1;31m Você já passou do tempo de alistamento\033[m , deveria ter se a listado há \033[1m {} anos\033[m'.format(tempo))
    alistar = date.today().year - tempo
    print('Você deveria ter se alistado em {}'.format(alistar))


