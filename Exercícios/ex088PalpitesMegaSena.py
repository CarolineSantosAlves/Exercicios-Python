from random import sample
from time import sleep
jogo = []
print('-=' * 30)
print('         JOGA NA MEGA SENA       ')
print('-=' * 30)
jogadas = int(input('Quantos jogos você quer que eu sorteie? '))
for p in range(jogadas):
    j = sorted(sample(range(1, 61), 6))
    jogo.append(j[:])
    print(f'jogo{p+1}:{j}')
    sleep(0.5)
print('-=-=-=-= BOA SORTE -=-=-=-=')

