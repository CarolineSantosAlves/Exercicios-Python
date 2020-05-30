frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra (a) aparece {} vezes na frase'.format(frase.count('a')))
print('A letra (a) aparece pela primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra (a) aparece pela ultima vez na posição {}'.format(frase.rfind('a')+1))