from time import sleep

print('-=-' * 20)
print('CAIXA ELETRÔNICO')
print('-=-' * 20)

saque = float(input('Informe o valor que deseja sacar!\n'
                    'Mínimo R$ 10,00\n'
                    'Máximo R$ 600,00\n'
                    'Notas disponíveis: R$1, R$5, R$10, R$50 e R$100\n'
                    'R$: '))
v1 = saque

if 10 <= saque <= 600:
    cem = int(v1 / 100)
    v1 = v1 - (cem * 100)

    cinq = int(v1 / 50)
    v1 = v1 - (cinq * 50)

    dez = int(v1 / 10)
    v1 = v1 - (dez * 10)

    cinco = int(v1 / 5)
    v1 = v1 - (cinco * 5)

    um = v1

    print('Para sacar R$ {:.2f} vc vai precisar de:'.format(saque))
    sleep(2)
    print('-' * 50)
    print('Notas de R$100: {}'.format(cem))
    print('Notas de R$50: {}'.format(cinq))
    print('Notas de R$10: {}'.format(dez))
    print('Notas de R$5: {}'.format(cinco))
    print('Notas de R$1: {}'.format(int(um)))
    print('-' * 50)

else:
    print('Informe um valor válido entre R$10,00 e R$600,00')
