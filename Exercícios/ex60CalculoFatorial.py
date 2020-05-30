#from math import factorial
#n = int(input('Quero fatorial de: '))
#fat = factorial(n)
#print(fat)
n = int(input('Quero fatorial de: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))