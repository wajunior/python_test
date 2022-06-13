c = 1
total = 0
ini = 's'


while c != 0:
    ini = str(input('Gostaria de iniciar venda? [S/N]: ')).lower()

    if ini == 's':
        d = 1
        while d != 0:

            prod = float(input('Informe o valor do produto {}: R$ '.format(d)))

            if prod != 0:
                d += 1
                total += prod
            else:
                print('Total: R$ {:.2f}'.format(total))
                din = float(input('Quantidade paga pelo cliente: R$ '))
                print('Dinheiro: R$ {:.2f}\n'
                      'Troco: R$ {:.2f}'.format(din, din - total))
                total = 0
                d = 0
    else:
        print('Saindo do programa!')
        c = 0


