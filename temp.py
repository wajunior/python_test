opc = int(input('Digite a oção desejada\n'
                '[1] Celcius / fahrenheit\n'
                '[2] Fahrenheit / Celcius\n'
                'Opção: '))

if opc == 1:
    cel = float(input('Digite a temperatura em Celcius: '))
    far = (cel * 9 / 5) + 32

    print('A temperatura em fahrenheit é {:.2f}'.format(far))
else:
    far = float(input('Digite a temperatura em fahrenheit: '))
    cel = (far - 32) * 5 / 9

    print('A temperatura em celcius é {:.2f}'.format(cel))
