lista = list()
r = 'S'
while r in 'Ss':
    lista.append(int(input('Digite um numero: ')))
    r = str(input('Quer continuar?[S/N] ')).strip().upper()
print(f'Voce digitou {len(lista)} numeros')
lista.sort(reverse=True)
print(f'Em ordem decrecente {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('Nao tem valor 5 na lista')
