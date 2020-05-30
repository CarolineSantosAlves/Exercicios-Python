produto = float(input('Valor do Produto: '))
print('''ESCOLHA A FORMA DE PAGAMENTO:
[1] A vista (Dinheiro/Cheque)
[2] A vista (Cartão)
[3] em até 2x no cartão
[4] 3x ou mais no cartão''')
pagamento = int(input('Sua escolha: '))
if pagamento == 1:
    vproduto = produto - (produto * 10 / 100)
elif pagamento == 2:
    vproduto = produto - (produto * 5 / 100)
elif pagamento == 3:
    parcela = produto / 2
    vproduto = produto
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif pagamento == 4:
    vproduto = produto + (produto * 20 / 100)
    parcela = int(input('Quantas parcelas? '))
    if parcela >= 3:
        print('Sua compra será parcelada em {} de R${:.2f} COM JUROS'.format(parcela, vproduto / parcela))

    else:
        print('Escolha 3 parcelas ou mais')
else:
    vproduto = produto
    print('\033[31m Digite uma opção de pagamento válida \033[m')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(produto, vproduto))

