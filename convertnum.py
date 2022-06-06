num = int(input('Informe um numero: '))

opt = int(input('Escolha para qual opção gostaria de converter o número.\n'
                '[1] - Binário.\n'
                '[2] - Octal.\n'
                '[3] - Hexadecimal.\n'
                ': '))

if opt == 1:
    print('Número Informado: {}\n'
          'Convertido para binário: {}'.format(num, format(num, 'b')))
elif opt == 2:
    print('Número Informado: {}\n'
          'Convertido para Octal: {}'.format(num, format(num, 'o')))
elif opt == 3:
    print('Número Informado: {}\n'
          'Convertido para Hexadecimal: {}'.format(num, format(num, 'x')))
