while True:
    print('-=' * 20)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-=' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n*c))
print("Programa de tabuada encerrado")
