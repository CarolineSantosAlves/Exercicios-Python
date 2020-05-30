funcionario = str(input('Funcionario: '))
salario = float(input('Digite o Salário do funcionário R$ '))
if salario > 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)

print('O novo salário do funcionário {} é R${:.2f}'.format(funcionario, aumento))
