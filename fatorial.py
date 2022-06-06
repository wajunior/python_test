opc = True

while opc:
    n = int(input('Informe o numero que gostaria de fatorar: '))
    mult = n

    if n < 0 or n > 16:
        print('Favor informar um numero correto!')
    else:
        print('{}'.format(n), end=' . ')
        while n > 1:
            n -= 1
            mult *= n
            print('{}'.format(n), end=' . ')

        print('= {}'.format(mult))

        op = str(input('\nGostaria de continuar? [S/N]: ')).lower()

        if op != 's':
            print('Saindo do programa!')
            opc = False


