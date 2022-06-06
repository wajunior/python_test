c = True

while c:
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))
    sal = float(input('Informe seu salario: '))
    sexo = input('Informe seu sexo [M] ou [F]: ').lower()
    estcivil = input('Informe seu estado civil\n'
                     '[s] - solteiro\n'
                     '[c] - casado\n'
                     '[v] - viuvo\n'
                     '[d] - divorciado\n'
                     ': ')
    if len(nome) > 3 and 0 < idade < 150 and sal > 0 and sexo == 'm' or sexo == 'f' and estcivil == 's' or estcivil == 'c' or estcivil == 'v' or estcivil == 'd':
        print('Nome: {}\n'
              'Idade: {}\n'
              'Salario: {:.2f}\n'
              'Sexo: {}\n'
              'Estado civil: {}'.format(nome, idade, sal, sexo, estcivil))
        c = False
    else:
        print('Valores não correspondem aos prerequisitos, informar novamente.')
