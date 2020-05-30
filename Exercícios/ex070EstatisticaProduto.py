soma = maismil = menorpreco = quant = 0
barato = ''
print('-=' * 30)
print('MERCADINHO AQUI TEM')
print('-=' * 30)
while True:
    prod = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    soma += preco
    quant += 1
    if preco >= 1000:
        maismil += 1
    if quant == 1 or preco < menorpreco:
        barato = prod
        menorpreco = preco

    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('--------------- FIM DO PROGRAMA -------------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {maismil} produtos custando R$1.000,00')
print(f'O produto mais barato foi {barato} que custa R${menorpreco:.2f}')
