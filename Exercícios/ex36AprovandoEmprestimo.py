casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos deseja pagar? '))
parcelas = anos * 12
vparcela = casa / parcelas
print('Você vai pagar {} parcelas de R${:.2f}'.format(parcelas, vparcela))
if vparcela > (salario * 30 / 100):
    print('\033[1;31m Emprestimo reprovado \033[m, o valor da parcela excede o permitido ')
else:
    print('\033[1;32m Empréstimo aprovado')

