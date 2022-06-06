#Calculo reajuste de salário

sal = float(input('Informe seu salário: R$ '))

if sal <= 280:
    novosal = sal + (sal * 20 / 100)
    print('Antigo Salario: R$ {:.2f}\n'
          'Porcentagem de aumento: 20%\n'
          'Valor do aumento: R$ {:.2f}\n'
          'Novo salário: R$ {:.2f}'.format(sal, (novosal - sal), novosal))
elif 280 < sal <= 700:
    novosal = sal + (sal * 15 / 100)
    print('Antigo Salario: R$ {:.2f}\n'
          'Porcentagem de aumento: 15%\n'
          'Valor do aumento: R$ {:.2f}\n'
          'Novo salário: R$ {:.2f}'.format(sal, (novosal - sal), novosal))
elif 700 < sal <= 1500:
    novosal = sal + (sal * 10 / 100)
    print('Antigo Salario: R$ {:.2f}\n'
          'Porcentagem de aumento: 10%\n'
          'Valor do aumento: R$ {:.2f}\n'
          'Novo salário: R$ {:.2f}'.format(sal, (novosal - sal), novosal))
else:
    novosal = sal + (sal * 5 / 100)
    print('Antigo Salario: R$ {:.2f}\n'
          'Porcentagem de aumento: 5%\n'
          'Valor do aumento: R$ {:.2f}\n'
          'Novo salário: R$ {:.2f}'.format(sal, (novosal - sal), novosal))
