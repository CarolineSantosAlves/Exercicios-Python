from random import randint
from random import choice
vitoria = empate = 0
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 20)
while True:
    nu = int(input('Diga um valor: '))
    nc = randint(0, 10)
    resultado = nu + nc
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print('-=' * 20)
    print(f'Você jogou {nu} e o computador jogou {nc}. O total de {resultado} ', end='')
    print('DEU PAR' if resultado % 2 == 0 else 'DEU IMPAR' )
    op = ['P', 'I']
    computador = choice(op).upper()
    if resultado % 2 == 0:
        resposta = 'P'
        if jogador == resposta:
            vitoria += 1
            print('VOCÊ VENCEU!')
            print('Vamos jogador novamente')
            print('-=' * 20)
        elif computador and jogador == resposta:
            empate += 1
            print('EMPATE')
            print('Vamos jogador novamente')

        else:
            print('VOCÊ PERDEU')
            break
    elif resultado % 2 == 1:
        resposta = 'I'
        if jogador == resposta:
            vitoria += 1
            print('VOCÊ VENCEU!')
            print('Vamos jogar novamente')
            print('-=' * 20)
        elif computador and jogador == resposta:
            empate += 1
            print('EMPATE')
            print('Vamos jogar novamente')
        else:
            print('Você perdeu')
            break

print(f'GAME Over! Você venceu {vitoria} vezes')
print(f'Total de empates {empate}')
print('-=' * 20)




