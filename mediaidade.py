c = 1
media = 0
soma = 0
total = 0

while c != 0:
    idd = int(input('Informe a idade da {}ª pessoa: '.format(c)))
    opc = str(input('Gostaria de informar mais idade? [S/N]: ')).lower()
    c += 1
    soma += idd
    media += 1

    if opc != 's':
        c = 0
    else:
        total = soma / media

print('A média de idade das pessoas informada é {:.2f}\n'
      'Portanto elas são: '.format(total))
if 0 < total <= 25:
    print('JOVEM!')
elif 25 < total <= 60:
    print('ADULTA!')
else:
    print('IDOSA')

