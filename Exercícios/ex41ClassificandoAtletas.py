from datetime import date
ano = int(input('Digite seu ano de Nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Categoria: \033[1;36m MIRIM')
elif idade <= 14:
    print('Categoria: \033[1;36m INFANTIL')
elif idade <= 19:
    print('Categoria: \033[1;36m JUNIOR')
elif idade <= 25:
    print('Categoria: \033[1;36m SÊNIOR')
else:
    print('Categoria: \033[1;36m MÂSTER')