from datetime import datetime
trabalhador = {}
trabalhador['Nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
trabalhador['idade'] = datetime.now().year - ano
trabalhador['carteira'] = int(input('Carteira de Trabalho(0 não tem): '))
if trabalhador['carteira'] != 0:
    trabalhador['contratacao'] = int(input('Ano de Contratação: '))
    trabalhador['salario'] = float(input('Salário: '))
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratacao'] + 35) - datetime.now().year)
for k, v in trabalhador.items():
    print(f'  -{k} tem o valor {v}')
