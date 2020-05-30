def notas(* nota, sit=False):
    """
    ->Função para analisar notas e situções de vários alunos.
    :param nota: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    avaliacao = dict()
    cont = maior = menor = soma = 0
    avaliacao['total'] = len(nota)
    for n in nota:
        if cont == 0:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n
        cont += 1
        soma += n
    avaliacao['maior'] = maior
    avaliacao['menor'] = menor
    avaliacao['media'] = soma / len(nota)
    if sit:
        if avaliacao['media'] >= 7:
            avaliacao['situação'] = 'BOA'
        elif 5 <= avaliacao['media'] < 7:
            avaliacao['situação'] = 'RAZOÁVEL'
        else:
            avaliacao['situação'] = 'RUIM'
    return avaliacao


#programa principal
resp = notas(2.5, 5.5, 4, 6.5)
print(resp)