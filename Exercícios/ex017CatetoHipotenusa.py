from math import hypot
co = float(input('Cateto Oposto: '))
ca = float(input('Cateto Adjacente: '))
h = hypot(co, ca)
print('A hipoitenusa vai medir {:.2f}'.format(h))