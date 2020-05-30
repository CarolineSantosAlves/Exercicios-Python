completa = []
impar = []
par = []
r = 'S'
while r in 'Ss':
    completa.append(int(input('Digite um numero: ')))
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
for v in completa:
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)
print(f'A lista completa é {completa}')
print(f'A listade impares é {impar}')
print(f'A lista dos pares é {par}')

