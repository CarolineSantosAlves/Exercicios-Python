nome = str(input('Nomes completo: ')).strip()
dividido = nome.split()
print('Nome Completo: {}'.format(nome))
print('Primeiro nome: {}'.format(dividido[0]))
print('Ultimo nome {}'.format(dividido[len(dividido) - 1]))