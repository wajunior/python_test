lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado:'))

if lado1 + lado2 == lado3 or lado1 + lado3 == lado2 or lado2 + lado3 == lado1:
    if lado1 == lado2 == lado3:
        print('Triangulo Equilatero!')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('Triangulo Isósceles!')
    elif lado1 != lado2 != lado3:
        print('Triangulo Escaleno')
else:
    print('Valores não formam um triângulo!')
