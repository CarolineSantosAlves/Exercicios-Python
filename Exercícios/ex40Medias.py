nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('\033[1;31m REPROVADO \033[m , sua média foi {:.2f}'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('\033[1;33m RECUPERAÇÃO \033[m , sua média foi {:.2f}'.format(media))
elif media >= 7.0:
    print('\033[1;32m APROVADO\033[m, sua média foi {:.2f}'.format(media))
