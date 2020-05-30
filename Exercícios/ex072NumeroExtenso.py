numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco',
           'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete',
           'Dezoito', 'Dezenove', 'Vinte')
cont = int(input('Digite um numero [0 a 20]: '))
while cont < 0 or cont > 20:
    cont = int(input('Tente novamente. Digite um numero [0 a 20]: '))
print(f'Você digtou o numero {numeros[cont]}')



