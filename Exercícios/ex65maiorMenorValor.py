r = 'S'
soma = quant = media = 0
while r in 'Ss':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Você digitou {} numeros e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
