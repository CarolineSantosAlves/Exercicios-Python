velo = float(input('Em que velocidade o carro está? '))
if velo > 80:
    multa = (velo - 80) * 7
    print('Você está acima da velocidade permitidade de 80 kmh e será multando em R${:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade permitida')
print('Bom dia , dirija com segurança')
