grupo = []
aluno = []
r = 'S'
while r in 'Ss':
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    grupo.append(aluno[:])
    aluno.clear()
    r = str(input('Quer continuar?[S/N] '))
print('-=' * 30)
print(f'Nº  NOME             MÉDIA')
print('-=' * 30)
for c, a in enumerate(grupo):
    print(f'{c}  {grupo[c][0]} {(grupo[c][1] + grupo[c][2]) / 2 }')
print('-=' * 30)
while True:
    n = int(input('Mostrar notas de qual Aluno?(999 interrompe): '))
    if n == 999:
        print('FINALIZANDO......')
        break
    if n <= len(grupo) - 1:
        print(f'Notas de {grupo[n][0]} são {grupo[n][1], grupo[n][2]} ')
print('<<< VOLTE SEMPRE >>>')




