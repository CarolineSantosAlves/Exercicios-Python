n = 0
soma = 0
cont = 0
while n != 999:
    n = int(input('Digite um numero: '))
    if n != 999:
        soma += n
        cont += 1
print('Voc soma dos numeros é {}'.format(soma))
