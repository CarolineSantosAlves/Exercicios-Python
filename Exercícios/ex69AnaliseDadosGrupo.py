mdezoito = homens = fvinte = 0
while True:
    print('-=' * 20)
    print('\033[33mCADASTRE UMA PESSOA\033[m')
    print('-=' * 20)
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F] ')).strip().upper()[0]
    idade = int(input('Idade: '))
    print('-=' * 20)
    if idade >= 18:
        mdezoito += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        fvinte += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar?[S/N] ')).upper()[0].strip()
    if r == 'N':
        break
print('===FIM DO PROGRAMA===')
print(f'Total de pessoas com mais de 18 anos:{mdezoito}')
print(f'Ao todos temos {homens} homens cadastrados')
print(f'E temos {fvinte} mulheres com menos de 20 anos')
