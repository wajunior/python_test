print('-=-' * 20)
print('POSTO DE COMBUSTÍVEL VILA VELHA')
print('-=-' * 20)

print('=' * 30)
print('GASOLINA: R$ 7,30\n'
      'ETANOL: R$ 5,52')
print('=' * 30)

opt = str(input('Informe o tipo de combustível.\n'
                '[E] - Etanol.\n'
                '[G] - Gasolina.\n'
                ': ')).strip().lower()

litros = float(input('Informe quantidade de litros abastecidos: '))
e = litros * 5.25
g = litros * 7.30

if opt == 'e':
    if litros <= 20:
        valor = e - (e * 3 / 100)
    else:
        valor = e - (e * 5 / 100)

    print('Informações de abastecimento!\n'
          'Tipo: Etanol\n'
          'Litros: {:.1f}\n'
          'Valor: R$ {:.2f}'.format(litros, valor))
else:
    if litros <= 20:
        valor = g - (g * 4 / 100)
    else:
        valor = g - (g * 6 / 100)

    print('Informações de abastecimento!\n'
          'Tipo: Gasolina\n'
          'Litros: {:.1f}\n'
          'Valor: R$ {:.2f}'.format(litros, valor))
