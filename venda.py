morango = float(input('Informe a quantidade em Kg de morango: '))
maca = float(input('Informe a quantidade em Kg de maçãs: '))
totalkg = morango + maca

print('=' * 30)

if totalkg <= 5:
    totalmor = morango * 2.50
    totalmac = maca * 1.80
    print('Morango Kg: {:.1f}\n'
          'Maçã Kg: {:.1f}\n'
          'Kg total: {:.1f}'.format(morango, maca, totalkg))

    print('=' * 30)

    print('Morango Kg (R$ 2,50): R$ {:.2f}\n'
          'Maçã Kg (R$ 1,80): R$ {:.2f}\n'
          'Total: R$ {:.2f}'.format(totalmor, totalmac, totalmor + totalmac))

elif 5 < totalkg <= 8:
    totalmor = morango * 2.20
    totalmac = maca * 1.50
    print('Morango Kg: {:.1f}\n'
          'Maçã Kg: {:.1f}\n'
          'Kg total: {:.1f}'.format(morango, maca, totalkg))

    print('=' * 30)

    print('Morango Kg (R$ 2,20): R$ {:.2f}\n'
          'Maçã Kg (R$ 1,50): R$ {:.2f}\n'
          'Total: R$ {:.2f}'.format(totalmor, totalmac, totalmor + totalmac))

elif totalkg > 8 or (morango * 2.20) + (maca * 1.80) > 25:
    totalmor = morango * 2.20
    totalmac = maca * 1.80
    total = (totalmor + totalmac) * 10 / 100

    print('Morango Kg: {:.1f}\n'
          'Maçã Kg: {:.1f}\n'
          'Kg total: {:.1f}'.format(morango, maca, totalkg))

    print('=' * 30)

    print('Morango Kg (R$ 2,20): R$ {:.2f}\n'
          'Maçã Kg (R$ 1,50): R$ {:.2f}\n'
          'Total: R$ {:.2f}\n'
          'Total com 10% de desconto: R$ {:.2f}'.format(totalmor, totalmac, totalmor + totalmac, totalmor + totalmac - total))
