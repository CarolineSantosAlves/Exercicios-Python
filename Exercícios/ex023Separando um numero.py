num = int(input('Digite um numero de até 4 digitos: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milha = num // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milha: {}'.format(milha))
