num = str(input('Informe um numero entre 0 e 999: '))

if 0 <= int(num) < 1000:
    if len(num) == 1:
        print('Unidade: {}'.format(num[0]))
    elif len(num) == 2:
        print('Unidade: {}\n'
              'Dezena: {}'.format(num[1], num[0]))
    elif len(num) == 3:
        print('Unidade: {}\n'
              'Dezena: {}\n'
              'Centena: {}'.format(num[2], num[1], num[0]))
else:
    print('Numero inválido.')