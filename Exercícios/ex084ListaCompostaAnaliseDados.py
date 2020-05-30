pessoa = list()
grupo = list()
maior = menor = 0
r = 'S'
while r in 'Ss':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()
    r = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
print('-=' * 30)
print(f'Foram cadastradas Total de {len(grupo)} pessoas')
print(f'O maior peso foi {maior}kg. Peso de: ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'{p[0]}', end='')
print()
print(f'O menor peso foi {menor}kg. Peso de: ', end='')
for p in grupo:
    if p[1] == menor:
        print(f'{p[0]}', end='')
