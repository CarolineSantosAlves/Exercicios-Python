altura = float(input('Digite sua altura(m): '))
peso = float(input('Digite seu peso(kg): '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25.0 <= imc < 30.0:
    print('Você está com sobrepeso')
elif 30.0 <= imc < 40.0:
    print('Você está obeso')
elif imc > 40.0:
    print('Você está com obesidade mórbida')

