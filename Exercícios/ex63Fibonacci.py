n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print(t1, t2, end=' ')
while cont <= n:
    t3 = t1 + t2
    cont += 1
    print(t3, end=' ')
    t1 = t2
    t2 = t3

