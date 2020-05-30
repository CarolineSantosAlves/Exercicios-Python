def area(l, c):
    area = l * c
    print(f'A àrea de um terreno {l} x {c} é de {area} mts²')


print('    CONTROLE DE TERRENOS    ')
print('----------------------------')
l = float(input('LARGURA(m): '))
c = float(input('COMPRIMENTO(m): '))
area(l, c)