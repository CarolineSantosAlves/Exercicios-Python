num = 0
valores = [[], []]
for n in range(0, 7):
    num = int(input(f'Digite o {n + 1}º valor: '))
    if num % 2 == 0:
        valores[0].append(num)
    else:
        valores[1].append(num)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram {valores[0]}')
print(f'Os valores impares digitados foram {valores[1]}')
