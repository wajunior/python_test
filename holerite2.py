# Feito por Wilson Junior
print('\033[1;32m#\033[m' * 30)
print('\033[1;34m{:^30}\033[m'.format('Cálculo Salário Líquido'))
print('\033[1;32m#\033[m' * 30)

# Informa os dados salarial do funcionário
salarioBruto = float(input('Informe o salário bruto do funcionário: R$ '))
descontos = float(input('Valor total descontado pela empresa em comum acordo.\n'
                        '(Ex: previdência privada, pensão): R$ '))
dependentes = int(input('Informe quantos dependentes: '))

# Calcula o INSS
if salarioBruto <= 1212.00:
    inss = salarioBruto * 7.5 / 100
elif 1212 < salarioBruto <= 2427.35:
    inss = (1212 * 7.5 / 100) + ((salarioBruto - 1212) * 9 / 100)
elif 2427.35 < salarioBruto <= 3641.03:
    inss = (1212 * 7.5 / 100) + ((2427.35 - 1212) * 9 / 100) + ((salarioBruto - 2427.35) * 12 / 100)
elif 3641.03 < salarioBruto <= 7087.22:
    inss = (1212 * 7.5 / 100) + ((2427.35 - 1212) * 9 / 100) + ((3641.03 - 2427.35) * 12 / 100) + ((salarioBruto -
                                                                                                    3641.03) * 14 / 100)
else:
    inss = 828.39

# Calcula os descontos para calcular o Imposto de Renda
descontosTotal = salarioBruto - inss

# Calcula o Imposto de Renda sem dependentes
if dependentes == 0:
    if descontosTotal <= 1903.98:
        irrf = 0
    elif 1903.98 < descontosTotal <= 2826.65:
        irrf = ((descontosTotal * 7.5 / 100) - 142.80)
    elif 2826.65 < descontosTotal <= 3751.05:
        irrf = ((descontosTotal * 15 / 100) - 354.80)
    elif 3751.05 < descontosTotal <= 4664.68:
        irrf = ((descontosTotal * 22.5 / 100) - 636.13)
    elif descontosTotal > 4664.68:
        irrf = ((descontosTotal * 27.5 / 100) - 869.36)

# Calcula o Imposto de Renda com dependentes
else:
    descdep = descontosTotal - (dependentes * 189.59)

    if descdep <= 1903.98:
        irrf = 0
    elif 1903.98 < descdep <= 2826.65:
        irrf = ((descdep * 7.5 / 100) - 142.80)
    elif 2826.65 < descdep <= 3751.05:
        irrf = ((descdep * 15 / 100) - 354.80)
    elif 3751.05 < descdep <= 4664.68:
        irrf = ((descdep * 22.5 / 100) - 636.13)
    elif descdep > 4664.68:
        irrf = ((descdep * 27.5 / 100) - 869.36)

# Calcula o salário Líquido
salarioLiquido = descontosTotal - irrf - descontos

print('\033[1;32m#\033[m' * 30)

print('Salário bruto: R$ {:.2f}\n'
      'Descontos: R$ {:.2f}\n'
      'Dependentes: {}\n'
      'INSS: R$ {:.2f}\n'
      'IRRF: R$ {:.2f}\n'
      '\033[1;32m==========================================\033[m\n'
      'Total de descontos: \033[31mR$ {:.2f}\033[m\n'
      '\033[1;32m==========================================\033[m\n'
      'Salário liquido: \033[32mR$ {:.2f}\033[m\n'
      '\033[1;32m==========================================\033[m'.format(salarioBruto, descontos, dependentes, inss,
                                                                          irrf, (inss + irrf + descontos),
                                                                          salarioLiquido))
print('\n\n\nFeito por: Wilson Junior')
