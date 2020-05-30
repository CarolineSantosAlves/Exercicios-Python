def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} no campeonato')


n = str(input('Nome do jogador: '))
g = int(input('Números de gols: '))
ficha(n, g)
