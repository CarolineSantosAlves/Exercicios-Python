valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}ª:')))
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior} na posição {valores.index(max(valores))} ')
print(f'O menor valor digitado foi {menor} na posição {valores.index(min(valores))}')
