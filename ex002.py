num = int(input('Digite um numero positivo ou negativo: '))

if num < 0:
    print('O numero {} é negativo'.format(num))
elif num == 0:
    print('Numero é {}'.format(num))
else:
    print('O numero {} é positivo'.format(num))