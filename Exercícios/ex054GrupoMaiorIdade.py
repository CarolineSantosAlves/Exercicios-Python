from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {} nasceu?: '.format(c)))
    if date.today().year - ano >= 21:
        maior += 1
    else:
        menor += 1
print('\033[1;34m {}\033[m pessoas já atingiram a maior idade e \033[1;34m {}\033[m pessoas ainda não atigiram a '
      'maior idade'.format(maior, menor))


