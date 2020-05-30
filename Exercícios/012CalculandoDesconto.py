preco = float(input('Digite o valor do produto: R$'))
vd = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção vai custar R${:.2f}'.format(preco, vd))