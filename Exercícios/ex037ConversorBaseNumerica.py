num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] convertter para HEXADECIMAL''')
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igaul a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente')
