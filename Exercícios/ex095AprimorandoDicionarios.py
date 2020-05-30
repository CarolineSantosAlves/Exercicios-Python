time = list()
jogador = {}
golp = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partida'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for j in range(jogador['partida']):
        golp.append(int(input(f'     Quantos gols na partida {j}? ')))
    jogador['golpartida'] = golp[:]
    jogador['total'] = sum(golp)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar?[S/N]? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('Erro responda apenas S ou N')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod  Nome            gols        total')
print('--' * 30)
for c, j in enumerate(time):
    print(f'{c} {j["nome"]}             {j["golpartida"]}           {j["total"]}')

while True:
    op = int(input('Mostrar dados de qual jogador? (999 para parar'))
    if op == 999:
        print('Finalizando.......')
        break
    if op <= len(time) - 1:
        print(f'LEVANTAMENTO DO JOGADOR {time[op]["nome"]}')
