s = str(input('Informe seu sexo: [F/M] ')).upper()[0] .strip()
while s not in 'MF':
    s = str(input('Dados inválidos. Por favor informe seu sexo: ')).strip().upper()
print('Seu sexo {} registrado com sucesso'.format(s))

