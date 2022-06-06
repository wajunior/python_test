#calculo reajuste de salario 2

salario = float(input('Informe seu salário/h: R$ '))
horas = float(input('Informe quantidade de horas trabalhadas no mês: '))

salbruto = salario * horas
sind = salbruto * 3 / 100
inss = salbruto * 10 / 100
fgts = salbruto * 11 / 100

if salbruto <= 900:
    print('Salario Bruto: R$ {:.2f}\n'
          '(-) IR (5%): Isento\n'
          '(-) INSS (10%): R$ {:.2f}\n'
          '(-) Sindicato (3%): R$ {:.2f}\n'
          'FGTS (11%): R$ {:.2f}\n'
          'Total de descontos: R$ {:.2f}\n'
          'Salário Líquido: R$ {:.2f}'.format(salbruto, inss, sind, fgts, (inss + sind), (salbruto - inss - sind)))
elif 900 < salbruto <= 1500:

    ir = salbruto * 5 / 100
    desc = ir + inss + sind
    desct = salbruto - ir - inss - sind

    print('Salario Bruto: R$ {:.2f}\n'
          '(-) IR (5%): R$ {:.2f}\n'
          '(-) INSS (10%): R$ {:.2f}\n'
          '(-) Sindicato (3%): R$ {:.2f}\n'
          'FGTS (11%): R$ {:.2f}\n'
          'Total de descontos: R$ {:.2f}\n'
          'Salário Líquido: R$ {:.2f}'.format(salbruto, ir, inss, sind, fgts, desc, desct))
elif 1500 < salbruto <= 2500:
    ir = salbruto * 10 / 100
    desc = ir + inss + sind
    desct = salbruto - ir - inss - sind

    print('Salario Bruto: R$ {:.2f}\n'
          '(-) IR (10%): R$ {:.2f}\n'
          '(-) INSS (10%): R$ {:.2f}\n'
          '(-) Sindicato (3%): R$ {:.2f}\n'
          'FGTS (11%): R$ {:.2f}\n'
          'Total de descontos: R$ {:.2f}\n'
          'Salário Líquido: R$ {:.2f}'.format(salbruto, ir, inss, sind, fgts, desc, desct))
else:
    ir = salbruto * 20 / 100
    desc = ir + inss + sind
    desct = salbruto - ir - inss - sind

    print('Salario Bruto: R$ {:.2f}\n'
          '(-) IR (20%): R$ {:.2f}\n'
          '(-) INSS (10%): R$ {:.2f}\n'
          '(-) Sindicato (3%): R$ {:.2f}\n'
          'FGTS (11%): R$ {:.2f}\n'
          'Total de descontos: R$ {:.2f}\n'
          'Salário Líquido: R$ {:.2f}'.format(salbruto, ir, inss, sind, fgts, desc, desct))
