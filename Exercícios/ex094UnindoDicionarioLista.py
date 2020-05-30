grupo = []
pessoa = {}
mulheres = []
acima = []
dados = []
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo[F/M]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'FM':
        print('ERRO! Digite apenas M ou F')
        pessoa['sexo'] = str(input('Sexo[F/M]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())
    resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'A) Ao todo temos {len(grupo)} pessoas cadastradas.')
media = soma / len(grupo)
print(f'B) A média de idade é de {media:5.2f} anos.')
for p in range(len(grupo)):
    if grupo[p]['sexo'] == 'F':
        mulheres.append(grupo[p]['nome'])
print(f'C) As mulheres cadastradas foram {mulheres}')
print(f'D) Lista de pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('ENCERRANDO')



