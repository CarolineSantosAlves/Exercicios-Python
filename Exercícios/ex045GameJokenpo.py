from random import randint
print('Bem vindo ao Game Jokenpô PY')
print('''Escolha sua jogada:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Jogada: '))
maquina = randint(1, 3)
if jogador == 1 and maquina == 1:
    jogador = 'PEDRA'
    maquina = 'PEDRA'
    print('EMPATE')
elif jogador == 1 and maquina == 2:
    jogador = 'PEDRA'
    maquina = 'PAPEL'
    print('Eu venci')
elif jogador == 1 and maquina == 3:
    jogador = 'PEDRA'
    maquina = 'TESOURA'
    print('Você venceu')
print('Eu escolhi {} e você escolheu {}'.format(maquina, jogador))
