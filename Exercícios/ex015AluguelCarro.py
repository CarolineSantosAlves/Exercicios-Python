dias = float(input('Qiuantos dias alugados? '))
km = float(input('Quantos km rodados? '))
vp = (km * 0.15) + (dias * 60)
print('O total a pagar é de R${:.2f}'.format(vp))