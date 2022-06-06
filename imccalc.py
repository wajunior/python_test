print('\033[31m-=-' * 20)  # colocando cores e estilo com \033[m
print('\033[1;32m {:^52}'.format('CALCULADORA DE IMC'))  # dando espaçamento com o {:^52}
print('\033[31m-=-\033[m' * 20)  # colocando cores e estilo com \033[m

# Coletando dados do usuário
sexo = int(input('Digite seu sexo, [1] para H ou [2] para M: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
idade = int(input('Digite sua idade: '))
pesoh = (72.7 * altura) - 58
pesom = (62.1 * altura) - 44.7

# Calcula o IMC do usuário e arredonda as cadas decimais para 2 após a virula
imc = round(peso / (altura * altura), 2)
att = int(input('\nDigite seu grau de atividade física:\n'
                '[0] para sedentário\n'
                '[1] para leve\n'
                '[2] para moderada\n'
                '[3] para ativo (todos os dias)\n'
                '[4] para muito ativo (todos os dias, até 2x ao dia\n'
                'informar valor: '))

# Informa sobre a tabela de IMC
print('\n MENOR QUE 18,5	MAGREZA	0\n '
      'ENTRE 18,5 E 24,9	NORMAL	0\n '
      'ENTRE 25,0 E 29,9	SOBREPESO	I\n '
      'ENTRE 30,0 E 39,9	OBESIDADE	II\n '
      'MAIOR QUE 40,0	OBESIDADE GRAVE	III\n')

# Condição de peso e IMC do usuário, qual ele se encaixa
if imc < 18.5:
    print('Seu IMC é {}'.format(imc))
    print('Você precisa ganhar peso, está em estado de magreza!')
elif 18.5 <= imc <= 24.9:
    print('Seu IMC é {}'.format(imc))
    print('Saudável, IMC normal!')
elif 25.0 <= imc <= 29.9:
    print('Seu IMC é {}'.format(imc))
    print('Você está em SOBREPESO I')
elif 30 <= imc <= 39.9:
    print('Seu IMC é {}'.format(imc))
    print('Você está em OBESIDADE II')
else:
    print('Seu IMC é {}'.format(imc))
    print('OBESIDADE GRAVE III')

# Informa quantidade de calorias por dia precisa para emagrecer caso seja Homem
if sexo == 1:
    # Calcula a Taxa de Metabolismo Basal e multiplica a altura de centimetros por metros
    tmb = float(((13.5 * peso) + (5 * altura * 100) - (6.76 * idade)) + 66.5)

    if att == 0:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.2) - 500), 2))
    elif att == 1:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.375) - 500), 2))
    elif att == 2:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.55) - 500), 2))
    elif att == 3:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.725) - 500), 2))
    elif att == 4:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.9) - 500), 2))

    # calcula o peso ideal e quantos Kg ele precisa perder
    if peso > pesoh:
        print('Seu peso ideal é: {:.1f}, você precisa perder {:.1f}Kg'.format(pesoh, peso - pesoh))
    else:
        print('Seu peso ideal é: {:.1f}, você precisa ganhar {:.1f}Kg'.format(pesoh, pesoh - peso))

# Informa quantidade de calorias por dia precisa para emagrecer caso seja Mulher
elif sexo == 2:
    # Calcula a Taxa de Metabolismo Basal e multiplica a altura de centimetros por metros
    tmb = float(((9.56 * peso) + (1.85 * altura * 100) - (4.68 * idade)) + 665)

    if att == 0:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.2) - 500), 2))
    elif att == 1:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.375) - 500), 2))
    elif att == 2:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.55) - 500), 2))
    elif att == 3:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.725) - 500), 2))
    elif att == 4:
        print('\nVocê precisa ingerir {} calorias por dia'.format(round((tmb * 1.9) - 500), 2))

    # calcula o peso ideal e quantos Kg ele precisa perder
    if peso > pesom:
        print('Seu peso ideal é: {:.1f}Kg, você precisa perder {:.1f}Kg'.format(pesom, peso - pesom))
    else:
        print('Seu peso ideal é: {:.1f}Kg, você precisa ganhar {:.1f}Kg'.format(pesom, pesom - peso))
