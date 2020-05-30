from random import sample

numeros = []


def sorteia(lista):
    lista.append(sorted(sample(range(0, 10), 5)))
    print(f'Sorteamos 5 valores da lista:{lista}')


def somapar(lista):
    total = 0
    for v in lista:
        if v % 2 == 0:
            total += v
    print(f'Somando os valores pares da {lista}, temos {total}')


sorteia(numeros)
somapar(numeros)

