print('-=' * 20)
print('{:^30}'.format('BANCO CSA'))
print('-=' * 20)
valor = int(input('Que valor você quer sacar? R$'))
cin = (valor // 50)
nvalor = valor % 50
if cin > 0:
    print(f'Total de {cin} células de R$50,00')
vint = nvalor // 20
nvalor = nvalor % 20
if vint > 0:
    print(f'Total de {vint} células de R$20,00')
dez = nvalor // 10
nvalor = nvalor % 10
if dez > 0:
    print(f'Total de {dez} células de R$10,00')
um = nvalor // 1
nvalor = nvalor % 1
if um > 0:
    print(f'Total de {um} células de R$1,00')
print('Volte sempre ao banco CSA!Tenha um bom dia')