num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('Primeiro numero é maior')
elif num2 > num1:
    print('Segundo numero é maior')
else:
    print('Não existe numero maior, os dois são iguais')