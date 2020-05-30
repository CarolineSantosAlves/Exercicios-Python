somaidade = 0
hvelho = 0
nomehomem = ''
menosvinte = 0
for p in range(1, 5):
    print('------ {}ª PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(f/m): ')).strip().lower()
    somaidade += idade
    if sexo == 'm':
        if idade > hvelho:
            hvelho = idade
            nomehomem = nome
    elif sexo == 'f':
        if idade < 20:
            menosvinte += 1


media = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(media))
print('A idade do homem mais velho é {} anos e seu nome é {}'.format(hvelho, nomehomem))
print('No grupo tem {} mulheres com menos de 20 anos'.format(menosvinte))

