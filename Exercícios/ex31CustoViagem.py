distancia = int(input('Digite a distancia da viagem em km: '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('A sua viagem será de {} KM e o preço ficou R${:.2f}'.format(distancia, preco))
