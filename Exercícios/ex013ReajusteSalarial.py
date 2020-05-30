salario = float(input('Digite o salário R$'))
sr = salario + (salario * 15 / 100)
print('O salário de R${:.2f} foi reajustado para R${:.2f}'.format(salario, sr))