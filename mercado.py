print('-=-' * 20)
print('SUPERMERCADO CAMPO BELO')
print('-=-' * 20)

print('Até 5Kg\n'
      'File Duplo: R$ 4,90/Kg\n'
      'Alcatra: R$ 5,90/Kg\n'
      'Picanha: R$ 6,90/Kg\n\n'
      'Acima de 5Kg\n'
      'File Duplo: R$ 5,80/Kg\n'
      'Alcatra: R$ 6,80/Kg\n'
      'Picanha: R$ 7,80/Kg')
print('-' * 30)

tipocarne = str(input('Informe o tipo de carne que gostaria de comprar\n'
                      'Limitado a apenas um tipo por cliente: ')).strip().lower()

if tipocarne == 'file' or tipocarne == 'alcatra' or tipocarne == 'picanha':

    tipopag = int(input('Informe a forma de pagamento\n'
                        '[1] - Dinheiro\n'
                        '[2] - Crédito\n'
                        '[3] - Débito\n'
                        '[4] - Cartão Campo Belo'
                        ': '))

    if tipocarne == 'file' and tipopag != 4:
        totalkg = float(input('Informe a quantidade em Kg: '))

        if totalkg <= 5:
            file = totalkg * 4.90
            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ 0,00\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, file, tipopag, file))
            print('=' * 30)

        else:
            file = totalkg * 5.80
            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ 0,00\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, file, tipopag, file))
            print('=' * 30)

    elif tipocarne == 'file' and tipopag == 4:
        totalkg = float(input('Informe a quantidade em Kg: '))

        if totalkg < 5:

            file = totalkg * 4.90
            desconto = file * 5 / 100

            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ {:.2f}\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, file, tipopag, desconto, file - desconto))
            print('=' * 30)

        else:
            file = totalkg * 5.80
            desconto = file * 5 / 100

            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ {:.2f}\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, file, tipopag, desconto, file - desconto))
            print('=' * 30)

    if tipocarne == 'alcatra' and tipopag != 4:
        totalkg = float(input('Informe a quantidade em Kg: '))

        if totalkg <= 5:
            alcatra = totalkg * 5.90
            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ 0,00\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, alcatra, tipopag, alcatra))
            print('=' * 30)

        else:
            alcatra = totalkg * 6.80
            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ 0,00\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, alcatra, tipopag, alcatra))
            print('=' * 30)

    elif tipocarne == 'alcatra' and tipopag == 4:
        totalkg = float(input('Informe a quantidade em Kg: '))

        if totalkg <= 5:

            alcatra = totalkg * 5.90
            desconto = alcatra * 5 / 100

            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ {:.2f}\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, alcatra, tipopag, desconto, alcatra - desconto))
            print('=' * 30)

        else:
            alcatra = totalkg * 6.80
            desconto = alcatra * 5 / 100

            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ {:.2f}\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, alcatra, tipopag, desconto, alcatra - desconto))
            print('=' * 30)

    if tipocarne == 'picanha' and tipopag != 4:
        totalkg = float(input('Informe a quantidade em Kg: '))

        if totalkg <= 5:
            picanha = totalkg * 6.90
            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ 0,00\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, picanha, tipopag, picanha))
            print('=' * 30)

        else:
            picanha = totalkg * 7.80
            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ 0,00\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, picanha, tipopag, picanha))
            print('=' * 30)

    elif tipocarne == 'picanha' and tipopag == 4:
        totalkg = float(input('Informe a quantidade em Kg: '))

        if totalkg <= 5:

            picanha = totalkg * 6.90
            desconto = picanha * 5 / 100

            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ {:.2f}\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, picanha, tipopag, desconto, picanha - desconto))
            print('=' * 30)

        else:
            picanha = totalkg * 7.80
            desconto = picanha * 5 / 100

            print('=' * 30)
            print('Produto: {}\n'
                  'Kg: {:.1f}\n'
                  'Valor total: R$ {:.2f}\n'
                  'Tipo de pagamento: {}\n'
                  'Valor desconto: R$ {:.2f}\n'
                  'Valor a pagar: R$ {:.2f}'.format(tipocarne, totalkg, picanha, tipopag, desconto, picanha - desconto))
            print('=' * 30)

else:
    print('Opção Inválida!')
