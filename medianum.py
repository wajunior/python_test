soma = 0

for c in range(1, 6):
    num = int(input('Informe o {}º valor: '.format(c)))
    soma += num

print('A soma de todos os valores é {}\n'
      'A média é {:.1f}'.format(soma, soma / 5))
