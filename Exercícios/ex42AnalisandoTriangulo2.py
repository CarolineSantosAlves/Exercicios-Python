r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))


if r1 < (r2 + r3) and r2 < r3 + r1 and r3 < r2 + r1:
    print('Os segmentos acima podem formar um triângulo ', end="")
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('Não é possivel formar um triangulo com essas medidas')
