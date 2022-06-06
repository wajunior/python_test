import math

print('-=-' * 12)
print('EQUAÇÃO DE SEGUNDO GRAU ax²+bx²+c')
print('-=-' * 12)

a = int(input('Informe o valor de "a": '))

if a == 0:
    print('Valor de "a" não pode ser 0, programa será encerrado!')
else:
    b = int(input('Informe o valor de "b": '))
    c = int(input('Informe o valor de "c": '))

    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        print('Valor de Delta = {}\n'
              'Não possui raiz.'.format(delta))
    elif delta == 0:
        print('Valor da raiz X = {}'.format(math.sqrt(delta)))
    else:
        y1 = (-(b) + math.sqrt(delta)) / 2 * a
        y2 = (-(b) - math.sqrt(delta)) / 2 * a

        print('O valor da equação é\n'
              'x = {} \n'
              'y¹ = {:.2f}\n'
              'y² = {:.2f}'.format(delta, y1, y2))
