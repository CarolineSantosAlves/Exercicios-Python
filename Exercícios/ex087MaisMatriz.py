matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac2 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}] '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        if c == 2:
            somac2 += matriz[l][c]
        if c == 0:
            maior = matriz[1][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]
    print()
maior
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {somac2}')
print(f'A maior valor da segunda linha é {maior}')

