from math import ceil
num = float(input('Informe um numero qualquer: '))
inteiro = ceil(num)

if num < inteiro:
    print('O valor de {:.2f} é decimal!'.format(num))
elif num == inteiro:
    print('O valor de {} é inteiro!'.format(num))
