jogador = {}
golp = []
jogador['nome'] = str(input('Nome do Jogador: '))
jogador['partida'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for j in range(jogador['partida']):
    golp.append(int(input(f'     Quantos gols na partida {j}? ')))
jogador['golpartida'] = golp[:]
jogador['total'] = sum(golp)
print('-=' * 30)
print(jogador)
for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partida"]} partidas')
for i, v in enumerate(jogador['golpartida']):
   print(f'  => na partida {i}, fez {v} gols')
print(f'Foi um Total de {jogador["total"]} gols')
