num = int(input('Informe o valor que gostaria de ver a tabuada: '))

print('Tabuada do {}'.format(num))
for cont in range(1, 11):
    x = num * cont
    print('{:^3} x {:^3} = {:^3}'.format(num, cont, x))
