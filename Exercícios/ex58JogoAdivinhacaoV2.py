from random import randint
from time import sleep  # faz esperar um pouco simulando um processamento

print('Estou pensando em um numero....Tente advinhar')
n = randint(0, 10)
num = 0
tentativas = 0
while n != num:
    num = int(input('Digite um valor [0  a 10]: '))
    print('PROCESSANDO....')
    sleep(3)
    tentativas += 1
    print('Errou, Tente novamente')
print('Parabens, eu pensei no numero {} e você digitou {}'.format(n, num))
print('Foram necessárias {} tentativas'. format(tentativas))