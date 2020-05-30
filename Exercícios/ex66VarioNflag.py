s = c = 0
while True:
    n = int(input('Digite um numero: (999 para parar) '))
    if n != 999:
        s += n
        c += 1
    else:
        break
print(f'Foram digitados {c} numeros e a soma entre ele é {s}')

