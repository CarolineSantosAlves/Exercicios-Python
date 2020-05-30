valor = tuple(int(input('Digite um valor: '))for i in range(4))
print(f'Você digitou os numeros{valor}')
print(f'O numero 9 aparace {valor.count(9)} vezes')
if 3 in valor:
    print(f'O numero 3 está na {valor.index(3)+1}ª posição')
else:
    print('Não foi digitado nenhum numero 3')
print('Os numeros pares: ', end='')
for n in valor:
    if n % 2 == 0:
        print(n)


