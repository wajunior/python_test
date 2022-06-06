cont = True

while cont:
    nota = int(input('Informe uma nota de 0 a 10: '))
    if 0 > nota or nota > 10:
        print('Valor inválido, digite novamente!')
    else:
        print('Valor informado {}'.format(nota))
        cont = False
        