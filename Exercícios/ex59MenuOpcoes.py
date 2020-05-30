from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digte o Segundo valor: '))
r = 0
while r != 5:
    print('----ESCOLHA A OPERAÇÃO----')
    print('''    [1]SOMAR  
    [2]MULTIPLICAR 
    [3]MAIOR 
    [4]NOVOS NUMEROS
    [5]SAIR DO PROGRAMA''')
    r = int(input('>>>>>>>>>> Sua escolha: '))
    if r == 1:
        print('A soma de {} + {} é {}'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('A Multiplicação entre {} * {} é {}'.format(n1, n2, n1 * n2))
    elif r == 3:
        if n1 > n2:
            print('O maior valor é {} e o menor é {}'.format(n1, n2))
        else:
            print('O maior valor é {} e o menor é {}'.format(n2, n1))
    elif r == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o Segundo valor: '))
    elif r == 5:
        print('FIM DO PROGRAMA')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Obrigado por usar nossa calculadora')
