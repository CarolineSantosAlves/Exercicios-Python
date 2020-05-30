times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio',
         'São Paulo', 'Atlético-MG', 'Atlético-PR', 'Cruzeiro',
         'Bota-fogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians',
         'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os cinco primeiro colocados são: {times[0 : 5]}')
print('-=' * 20)
print(f'Os 4 ultimos são: {times[16::]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')