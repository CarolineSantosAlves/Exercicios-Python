from random import randint
from time import sleep #faz esperar um pouco simulando um processamento
print('Vou pensar em um numero, tente adivinhar')
num = int(input('Digite um numero de 0 a 5: '))
n = randint(0, 5)
print('PROCESSANDO....')
sleep(3)
if num == n:
    print('O numero que eu pensei foi {} e você digitou {}. Parabêns você acertou'.format(n, num))
else:
    print('Não foi desse vez, eu pensei no numero {} e você digitou {}'. format(n, num))


