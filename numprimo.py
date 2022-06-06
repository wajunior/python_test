n = int(input('Informe um numero para saber se ele é primo: '))
primo = 0

print('Valores divisíveis:')
for c in range(1, n+1):
    if n % c == 0:
        primo += 1
        print('\033[31m', end='')
    else:
        print('\033[33m', end='')

    print('{}'.format(c), end=' ')

print('\033[m\n')
if primo == 2:
    print('O valor {} é primo'.format(n))
else:
    print('O valor {} não é primo'.format(n))

print('Pois ele foi divisível {}x'.format(primo))
