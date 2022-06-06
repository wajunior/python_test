sal = float(input('Informe quanto vc ganha por mês: R$ '))
hr = float(input('Informe a quantidade de horas trabalhadas no mês: '))
salb = sal / hr
inss = sal * 9.06 / 100
ir = (sal - inss) * 2.43 / 100
# sind = salb * 5 / 100
salli = sal - ir - inss

print('+ Salário bruto: R$ {:.2f}\n'
      'Salário por hora: R$ {:.2f}\n'
      '- IR: R$ {:.2f}\n'
      '- INSS: R$ {:.2f}\n'
      'Total de descontos: R$ {:.2f}\n'
      '= Salário líquido: R$ {:.2f}'.format(sal, salb, ir, inss, sal - salli, salli))
