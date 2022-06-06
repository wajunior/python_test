from math import ceil

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))
opt = int(input('Escolha uma opção.\n'
                '[1] - Par ou Impar.\n'
                '[2] - Positivo ou Negativo.\n'
                '[3] - Inteiro ou Decimal.\n'
                ': '))

# Calcula se os numeros são pares ou impares
if opt == 1:

    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Os numeros {} e {} são pares!'.format(int(n1), int(n2)))
    elif n1 % 2 != 0 and n2 % 2 == 0:
        print('O numero {} é impar e o {} é par!'.format(int(n1), int(n2)))
    elif n1 % 2 == 0 and n2 % 2 != 0:
        print('O numero {} é par e o numero {} é impar!'.format(int(n1), int(n2)))
    elif n1 % 2 != 0 and n2 % 2 != 0:
        print('Os numeros {} e {} são impares!'.format(int(n1), int(n2)))

# Calcula se é positivo ou negativo
elif opt == 2:
    if n1 < 0 and n2 < 0:
        print('Numeros {} e {} são negativos!'.format(int(n1), int(n2)))
    elif n1 >= 0 and n2 >= 0:
        print('Numeros {} e {} são positivos!'.format(int(n1), int(n2)))
    elif n1 < 0 and n2 >= 0:
        print('Numero {} é negativo e {} positivo!'.format(int(n1), int(n2)))
    elif n1 >= 0 and n2 < 0:
        print('Numero {} é positivo e {} é negativo.'.format(int(n1), int(n2)))

# Informa se o numero é inteiro ou decimal
elif opt == 3:
    int1 = ceil(n1)
    int2 = ceil(n2)

    if n1 < int1 and n2 < int2:
        print('Numeros {:.2f} e {:.2f} são decimais!'.format(n1, n2))
    elif n1 == int1 and n2 == int2:
        print('Numeros {} e {} são inteiros!'.format(n1, n2))
    elif n1 < int1 and n2 == int2:
        print('Numero {:.2f} é decimal e {} é inteiro!'.format(n1, n2))
    elif n1 == int1 and n2 < int2:
        print('Numero {} é inteiro e {:.2f} é decimal!'.format(n1, n2))

else:
    print('Opção incorreta!')
