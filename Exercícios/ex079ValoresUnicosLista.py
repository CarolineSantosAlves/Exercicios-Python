valores = list()
r = 'S'
while r in 'Ss':
    n = int(input('Digite um numero: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado nao vou adicionar')
    r = str(input('Quer continuar?[S/N] ')).strip().upper()
valores.sort()
print(f'voce digitou os valores{valores}')
