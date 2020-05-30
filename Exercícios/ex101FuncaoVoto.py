def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos: ', end='')
    if idade < 18:
        return 'NAO VOTA'
    elif idade >= 18 and idade < 65:
        return 'VOTO OBRIGATÓRIO'
    else:
        return 'VOTO OPCIONAL'


ano = int(input('Digite o ano de Nascimento: '))
print(voto(ano))
