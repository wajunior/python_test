cd = int(input('Informe a quantidade de CDs: '))
qtd = 0
total = 0

for c in range(1, cd+1):
    valor = float(input('Informe o valor do {}º CD: R$ '.format(c)))
    total += valor
    qtd += 1

print('Quantidade de CDs: {}\n'
      'Valor total da coleção: R$ {:.2f}\n'
      'Valor médio da coleção: R$ {:.2f}'.format(qtd, total, total / qtd))
